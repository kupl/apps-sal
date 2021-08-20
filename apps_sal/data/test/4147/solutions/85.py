(n, a, b, c) = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))
m = [a, b, c]
ans = 4000
for i in range(4 ** n):
    p = [0] * n
    k = i
    for j in range(n):
        p[j] = k % 4
        k //= 4
    cost = [-1, -1, -1]
    q = [[] for _ in range(4)]
    for j in range(n):
        q[p[j]].append(l[j])
    for j in range(3):
        if len(q[j + 1]) != 0:
            cost[j] = 10 * (len(q[j + 1]) - 1) + abs(sum(q[j + 1]) - m[j])
    if cost[0] != -1 and cost[1] != -1 and (cost[2] != -1):
        ans = min(ans, cost[0] + cost[1] + cost[2])
print(ans)
