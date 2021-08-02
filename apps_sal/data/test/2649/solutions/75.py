n = int(input())
k = [0] * n
l = [0] * n
for i in range(n):
    x, y = [int(i) for i in input().split()]
    k[i] = x + y
    l[i] = x - y
print(max(max(k) - min(k), max(l) - min(l)))
