(n, l, a) = list(map(int, input().split()))
(ans, prev) = (0, 0)
for i in range(n):
    (t, tr) = list(map(int, input().split()))
    if i == 0:
        ans += t // a
    else:
        ans += (t - prev) // a
    prev = t + tr
ans += (l - prev) // a
print(ans)
