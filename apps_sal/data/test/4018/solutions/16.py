(n, setsize) = list(map(int, input().split()))
s = input()
count = [[0 for j in range(n + 1)] for i in range(n + 1)]
for i in range(n):
    j = i - 1
    while j >= 0:
        for k in range(1, n):
            count[i][k + 1] += count[j][k]
        if s[j] == s[i]:
            break
        j -= 1
    if j == -1:
        count[i][1] += 1
cost = 0
count[0][0] = 1
for l in range(n, -1, -1):
    if setsize == 0:
        break
    ct = 0
    localcost = n - l
    for i in range(n):
        ct += count[i][l]
    minct = min(setsize, ct)
    setsize -= minct
    cost += minct * localcost
if setsize == 0:
    print(cost)
else:
    print(-1)
