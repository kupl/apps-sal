n = int(input())
l = list([tuple(map(int, input().split())) for x in range(n)])
(p, q) = list(map(sum, list(zip(*l))))
o = abs(p - q)
(a, ai) = (o, 0)
for i in range(n):
    (u, v) = l[i]
    p += v - u
    q += u - v
    if abs(p - q) > a:
        (a, ai) = (abs(p - q), i + 1)
    p -= v - u
    q -= u - v
print(ai)
