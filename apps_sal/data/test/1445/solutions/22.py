n = int(input().strip())
a = input().strip().split()
for i in range(n // 2):
    if i % 2 == 0:
        (a[i], a[n - i - 1]) = (a[n - i - 1], a[i])
print(' '.join(a))
