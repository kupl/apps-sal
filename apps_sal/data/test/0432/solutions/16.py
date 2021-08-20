n = int(input())
c = [0] + list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
g = [0] * (n + 1)
answer = 0
for i in range(1, n + 1):
    node = i
    while g[node] == 0:
        g[node] = i
        node = a[node]
    if g[node] != i:
        continue
    current = node
    min_cost = c[node]
    while a[node] != current:
        node = a[node]
        min_cost = min(min_cost, c[node])
    answer += min_cost
print(answer)
