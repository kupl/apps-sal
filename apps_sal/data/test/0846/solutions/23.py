(n, m) = tuple(map(int, input().split()))
b = list(map(int, input().split()))
a = [0] * n
for i in b:
    for j in range(i - 1, n):
        if a[j] == 0:
            a[j] = str(i)
print(' '.join(a))
