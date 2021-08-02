n = int(input())
a, p = [], []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    p.append(y)

cur_min = float('inf')
cost = 0

for i in range(n):
    cur_min = min(cur_min, p[i])
    cost += cur_min * a[i]
print(cost)
