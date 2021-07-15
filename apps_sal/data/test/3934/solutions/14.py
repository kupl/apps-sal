n = int(input())
a, flag = [0] * (n + 1), False
for i in range(n - 1):
    u, v = [int(x) for x in input().split()]
    a[u] += 1
    a[v] += 1
for j in range(1, n + 1):
    if a[j] == 2:
        flag = True
if flag:
    print("NO")
else:
    print("YES")

