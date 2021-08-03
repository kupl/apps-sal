n, m, x = map(int, input().split())
a = list(map(int, input().split()))
data = [0] * (n + 1)
cost_1 = 0
cost_2 = 0
for i in range(m):
    data[a[i]] = 1
for i in range(0, x):
    cost_1 += data[i]
for j in range(x, n):
    cost_2 += data[j]
print(min(cost_1, cost_2))
