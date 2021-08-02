n, k = map(int, input().split())

L = list(range(1, n + 1))

for i in range(-1, -k - 1, -1):
    print(L[i], end=" ")
for i in range(n - k):
    print(L[i], end=" ")
