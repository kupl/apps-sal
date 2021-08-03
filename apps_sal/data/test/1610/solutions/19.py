n, k = map(int, input().split())

l = [0] * n
for i in range(n, n - k, -1):
    l[n - i] = i
for i in range(1, n - k + 1):
    l[i + k - 1] = i
for i in range(n):
    print(l[i], end=" ")
