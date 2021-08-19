(n, *a) = map(int, open(0).read().split())
b = [0] * (n + 1)
for i in range(1, n + 1)[::-1]:
    b[i] += (sum((b[j] for j in range(i, n + 1, i))) + a[i - 1]) % 2
print(sum(b))
print(*[i for i in range(n + 1) if b[i] > 0])
