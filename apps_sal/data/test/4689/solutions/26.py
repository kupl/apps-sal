(k, n) = map(int, input().split())
A = list(map(int, input().split()))
a = A
for i in range(n):
    a.append(k + A[i])
d = [0] * n
for i in range(n):
    d[i] = a[n - 1 + i] - a[i]
print(min(d))
