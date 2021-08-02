n = int(input())
k = int(-0.4999999 + (0.25 + 2 * n)**0.5)
print(k)
for i in range(1, k):
    print(i, end=" ")
print(n - k * (k - 1) // 2)
