n = int(input())
p = 1
q = 1
for i in range(n):
    (t, a) = map(int, input().split())
    f = max((p + t - 1) // t, (q + a - 1) // a)
    p = t * f
    q = a * f
print(p + q)
