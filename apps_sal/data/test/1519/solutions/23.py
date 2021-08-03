n, l, a = list(map(int, input().split()))
c = 0
p = 0
for _ in range(n):
    t, per = list(map(int, input().split()))
    c += (t - p) // a
    p = t + per
c += (l - p) // a
print(c)
