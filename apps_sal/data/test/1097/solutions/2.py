(n, t, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
p = {}
cnt = 0
cur = 1
floor = [[1]]
for ak in a:
    arr = [cur + i for i in range(1, ak + 1)]
    floor.append(arr)
    cur += ak
for i in range(1, t + 1):
    cnt += len(floor[i]) - 1
    if i == t:
        cnt += 1
    for u in floor[i]:
        p[u] = floor[i - 1][0]
for i in range(2, t + 1):
    if cnt <= k:
        break
    j = 1
    min_ = min(len(floor[i]), len(floor[i - 1]))
    while j < min_ and cnt > k:
        p[floor[i][j]] = floor[i - 1][j]
        cnt -= 1
        j += 1
if cnt == k:
    print(n)
    print('\n'.join([str(u) + ' ' + str(v) for (u, v) in list(p.items())]))
else:
    print(-1)
