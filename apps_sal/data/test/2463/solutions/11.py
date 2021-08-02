n = int(input())
u = sorted(list(map(int, input().split())))
print((n - 1) // 2)
ans = []
ind = 0
for i in range((n - 1) // 2, n):
    ans.append(u[i])
    if ind == (n - 1) // 2:
        continue
    ans.append(u[ind])
    ind += 1
print(' '.join(map(str, ans)))
