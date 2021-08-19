(n, k) = input().split()
(n, k) = (int(n), int(k))
for i in range(k + 1):
    print(k + 1 - i, end=' ')
for i in range(k + 2, n + 1):
    print(i, end=' ')
