n = int(input())
lis = []
for _ in range(n):
    tt, ww = [int(x) for x in input().split()]
    lis.append((tt, -ww))
lis.sort()
sum1, sum2 = [0], [0]
for i in range(n):
    if lis[i][0] == 1:
        sum1.append(sum1[-1] - lis[i][1])
    else:
        sum2.append(sum2[-1] - lis[i][1])
ans = 1000000000
k1, k2 = len(sum1) - 1, len(sum2) - 1
v = k2 + 1
for u in range(0, k1 + 1):
    while v - 1 >= 0 and 2 * (v - 1) + sum2[v - 1] >= sum1[k1] + sum2[k2] - sum1[u] - u:
        v -= 1
    if v <= k2:
        ans = min(ans, u + 2 * v)
print(ans)
