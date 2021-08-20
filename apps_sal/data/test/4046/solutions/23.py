n = int(input())
a = [int(t) for t in input().split(' ')]
b = [0] * n
b[1] = a[0]
for i in range(0, n - 1):
    b[i + 1] = b[i] + a[i]
m = min(b)
for i in range(n):
    b[i] -= m
    b[i] += 1
if len(set(b)) != n or any((t > n or t < 1 for t in b)):
    print(-1)
else:
    print(*b)
