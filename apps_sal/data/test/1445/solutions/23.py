n = int(input())
z = list(map(int, input().strip().split()))
for i in range(n // 2):
    if i % 2 == 0:
        z[i], z[n - i - 1] = z[n - i -1], z[i]
print(' '.join(list(map(str, z))))
