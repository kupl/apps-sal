n = int(input())
a = sorted(map(int, input().split()))
print((n - 1) // 2)
for i in range(n):
    print(a[(1 - i % 2) * (n // 2) + i // 2], end=' ')
