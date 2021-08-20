n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = 2 * ((a[i] - 1) // 2) + 1
print(' '.join(map(str, a)))
