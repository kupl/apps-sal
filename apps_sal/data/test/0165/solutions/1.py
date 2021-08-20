def c(ans, b, d, s):
    return min(ans, 3 * max(b, d, s) - b - d - s)


(b, d, s) = list(map(int, input().split()))
ans = 10 ** 19
m = min(b, d, s)
b = b - m
d = d - m
s = s - m
if b > 0:
    b -= 1
    ans = c(ans, b, d, s)
    b += 1
if d > 0:
    d -= 1
    ans = c(ans, b, d, s)
    d += 1
if s > 0:
    s -= 1
    ans = c(ans, b, d, s)
    s += 1
if b * d > 0:
    b -= 1
    d -= 1
    ans = c(ans, b, d, s)
    b += 1
    d += 1
if b * s > 0:
    b -= 1
    s -= 1
    ans = c(ans, b, d, s)
    b += 1
    s += 1
if s * d > 0:
    s -= 1
    d -= 1
    ans = c(ans, b, d, s)
    s += 1
    d += 1
if b + d + s == 0:
    ans = 0
print(ans)
