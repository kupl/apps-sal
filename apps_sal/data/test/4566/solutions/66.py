n, m = map(int, input().split())
ar = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    ar[a - 1] += 1
    ar[b - 1] += 1
for i in range(n):
    print(ar[i])
