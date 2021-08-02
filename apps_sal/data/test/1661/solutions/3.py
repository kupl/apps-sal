n, m = list(map(int, input().split()))
c = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0
for k in c:
    if not a:
        break
    if a[0] >= k:
        ans += 1
        a.pop(0)
print(ans)
