n = int(input())
(s, p, q) = (0, [0] * n, [0] * n)
for i in range(n):
    (p[i], q[i]) = [int(x) for x in input().split()]
    if q[i] - p[i] > 1:
        s += 1
print(s)
