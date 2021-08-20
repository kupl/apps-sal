3


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


x = input()
x = [int(_) for _ in x.split()]
t = x[0]
w = x[1]
b = x[2]
x = gcd(w, b)
k = min(w, b)
lcm = w * b // x
alpha = t // lcm
ans = alpha * k
l = alpha * lcm + k - 1
if l <= t:
    ans += k
else:
    ans += t - alpha * lcm + 1
ans -= 1
gg = gcd(ans, t)
ans = ans // gg
t = t // gg
print(str(ans) + '/' + str(t))
