ans = {}
(n, k) = (int(s) for s in input().split())
l = [int(s) for s in input().split()]
l.sort()
for i in range(n):
    x = l[i]
    count = 0
    while x > 0:
        if x in ans:
            if ans[x][0] < k:
                ans[x][0] += 1
                ans[x][1] += count
        else:
            ans[x] = [1, count]
        count += 1
        x = x // 2
    if 0 in ans:
        if ans[0][0] < k:
            ans[0][0] += 1
            ans[0][1] += count
    else:
        ans[x] = [1, count]
ansm = 1000000000007
for i in ans:
    if ans[i][0] >= k:
        ansm = min(ansm, ans[i][1])
print(ansm)
