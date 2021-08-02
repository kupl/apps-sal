M, K = map(int, input().split())
if M == 0 and K == 0:
    ans = [0, 0]
elif M == 1:
    if K == 0:
        ans = [0, 0, 1, 1]
    else:
        ans = [-1]
elif K >= 2**M:
    ans = [-1]
else:
    ans = []
    for i in range(2**M):
        if i != K:
            ans.append(i)
    ans.append(K)
    for j in range(2**M - 1, -1, -1):
        if j != K:
            ans.append(j)
    ans.append(K)
for i in ans:
    print(i, end=' ')
