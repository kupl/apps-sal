n, m, w = list(map(int, input().split()))
t = list(map(int, input().split()))

def check(x):
    p = [0] * w
    d = s = j = 0
    for i in t:
        d -= p[j]
        q = max(0, x - i - d)
        d += q
        s += q
        p[j] = q
        j += 1
        if j == w: j = 0
    return s

a = min(t)
b = a + m + 1
while b - a > 1:
    c = (a + b) // 2
    p = check(c)
    if p > m: b = c
    else: a = c
print(a)

