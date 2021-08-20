n = int(input())
(t0, a0) = (1, 1)
for i in range(n):
    (t1, a1) = map(int, input().split())
    f0 = t0 // t1
    if t0 % t1 != 0:
        f0 += 1
    f1 = a0 // a1
    if a0 % a1 != 0:
        f1 += 1
    f = max(f0, f1)
    (t0, a0) = (t1 * f, a1 * f)
print(t0 + a0)
