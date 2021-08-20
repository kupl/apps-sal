import math
(n, a, b) = list(map(int, input().split()))
target = 6 * n
if target < a * b:
    p = a
    q = b
else:
    m = int(target ** 0.5) + 1
    s = (a + m) * (b + m)
    for i in range(a, m):
        bb = max(math.ceil(target / i), b)
        if i * bb < s:
            s = i * bb
            p = i
            q = bb
    for j in range(b, m):
        aa = max(math.ceil(target / j), a)
        if j * aa < s:
            s = j * aa
            p = aa
            q = j
print(p * q)
print(p, q)
