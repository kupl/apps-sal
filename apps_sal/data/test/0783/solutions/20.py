n = int(input())
a = [int(x) for x in input().split()]
m = [0 for x in range(n)]
m[n - 1] = a[n - 1]
for i in range(n - 2, -1, -1):
    m[i] = max(m[i + 1], a[i])
for i in range(n - 1):
    print(max(0, m[i + 1] + 1 - a[i]), end=' ')
print(0)
