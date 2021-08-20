(n, k) = map(int, input().split())
print(int((n * (k - 1) + 1 + (n - 1) * (n - k + 1) / 2) * n))
for i in range(n):
    curr = []
    for j in range(n):
        if j + 1 == k:
            curr.append(n * (k - 1) + 1 + i * (n - k + 1))
        elif j + 1 > k:
            curr.append(n * (k - 1) + 1 + i * (n - k + 1) + (j + 1 - k))
        else:
            curr.append(i * (k - 1) + j + 1)
    print(' '.join(map(str, curr)))
