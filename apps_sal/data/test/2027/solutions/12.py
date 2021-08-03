n = int(input())
a = list(map(int, input().split()))
b = [0] * n
b[n - 1] = a[n - 1]

for i in range(n - 2, -1, -1):
    b[i] = a[i] + a[i + 1]

print(*b)
