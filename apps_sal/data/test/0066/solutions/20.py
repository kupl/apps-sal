t, a, b = list(map(int, input().split()))


def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a // gcd(a, b) * b


l = lcm(a, b)
last = t // l * l
ans = t // l * min(a, b)
ans += min(a, b, t - last + 1)
ans -= 1
g = gcd(ans, t)
ans //= g
t //= g
ans = str(ans) + '/' + str(t)
print(ans)
