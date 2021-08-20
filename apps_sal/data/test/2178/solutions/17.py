n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
mp = {}
f = 0
for i in range(n):
    mp[a[i]] = i + 1
ans = []
for i in range(n):
    if mp[b[i]] > f:
        ans.append(mp[b[i]] - f)
        f = mp[b[i]]
    else:
        ans.append(0)
print(*ans)
