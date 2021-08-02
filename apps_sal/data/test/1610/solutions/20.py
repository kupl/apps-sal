n, k = [int(x) for x in input().split()]
for i in range(n - k - 1):
    print(i + 1, end=' ')
for i in range(k + 1):
    print(n - i, end=' ')
print()
