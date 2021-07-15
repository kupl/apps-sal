R = lambda :map(int, input().split())
n, m = R()
a = list(R())
b = list(R())
li = []
cost = 0
for i in range(1, n + 1):
    if i not in b:
        cost += a[i - 1]
    else:
        li.append(a[i - 1])
li.sort(reverse=True)
for i in range(m):
    cost += max(cost, li[i])
print(cost)
