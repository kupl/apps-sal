(N, T) = map(int, input().split())
t = list(map(int, input().split()))
(ans, now) = (0, 0)
for i in t:
    if i < now:
        ans -= now - i
    ans += T
    now = i + T
print(ans)
