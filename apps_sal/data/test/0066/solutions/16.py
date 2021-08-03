t, w, b = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a // gcd(a, b) * b


add = min(w, b) - 1
l = lcm(w, b)

cnt = t // l

ans = add + cnt + cnt * add
ans -= max(0, l * cnt + add - t)

g = gcd(ans, t)
if g != 0:
    ans //= g
    t //= g

print(ans, end='')
print('/', end='')
print(t)
