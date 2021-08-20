(n, m) = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = (a[i] + m - 1) // m
x = max(a)
print(n - a[::-1].index(x))
