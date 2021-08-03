n = int(input())
a = list(map(int, input().split()))

x = [0] * n

x[0] = sum(a) - 2 * (sum(a[1::2]))
for i in range(n - 1):
    x[i + 1] = 2 * a[i] - x[i]

print(*x, end="")
