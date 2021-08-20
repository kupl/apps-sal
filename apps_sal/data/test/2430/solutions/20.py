n = int(input())
a = []
for i in range(n):
    a += [int(input())]
print(2 * n - 1 + a[0] + sum((abs(a[i] - a[i - 1]) for i in range(1, n))))
