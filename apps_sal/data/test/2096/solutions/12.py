n = int(input())
arr = list(map(int, input().split()))
adj = [[] for i in range(100)]
for i in range(2 * n):
    adj[arr[i]].append(i)
res = [0] * (2 * n)
(mul, curr) = ([], 1)
x = [0, 0]
for i in range(10, 100):
    if len(adj[i]) == 1:
        res[adj[i][0]] = curr
        x[curr - 1] += 1
        curr = 3 - curr
    if len(adj[i]) > 1:
        res[adj[i][0]] = 1
        res[adj[i][1]] = 2
        x[0] += 1
        x[1] += 1
        for j in range(2, len(adj[i])):
            mul.append(adj[i][j])
for i in range(len(mul)):
    res[mul[i]] = curr
    curr = 3 - curr
print(x[0] * x[1])
print(*res)
