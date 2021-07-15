n = int(input())
a = [0] * (n + 1)
for i in range(n - 1):
    v1, v2 = [int(i) for i in input().split()]
    a[v1] += 1
    a[v2] += 1
print(a.count(1))

