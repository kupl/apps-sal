(n, t) = list(map(int, input().split()))
l = list(map(int, input().split()))
now = 0
latest = 0
ans = 0
for i in l:
    now = i
    if now - latest >= t:
        ans += t
    else:
        ans += now - latest
    latest = now
ans += t
print(ans)
