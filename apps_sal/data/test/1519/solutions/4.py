(n, L, a) = map(int, input().split())
last_time = 0
res = 0
for i in range(n):
    (t, l) = map(int, input().split())
    res += (t - last_time) // a
    last_time = t + l
res += (L - last_time) // a
print(res)
