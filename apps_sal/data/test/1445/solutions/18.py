n = int(input())
a = [int(el) for el in input().split()]

for i in range(0, n // 2, 2):
    a[i], a[n - i - 1] = a[n - i - 1], a[i]

print(' '.join([str(el) for el in a]))
