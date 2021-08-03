k = int(input())
n = 50

i = k % 50
j = k // 50

print(50)
for _ in range(n - i):
    print(n + j - i - 1, end=' ')
for _ in range(i):
    print(2 * n + j - i, end=' ')
