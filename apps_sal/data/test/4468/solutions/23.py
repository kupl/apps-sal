(n, t) = map(int, input().split())
T = list(map(int, input().split()))
(prev, now, ans) = (T[0], 0, 0)
for i in range(n):
    if not i:
        continue
    now = T[i]
    if now - prev > t:
        ans += t
    else:
        ans += now - prev
    prev = now
ans += t
print(ans)
