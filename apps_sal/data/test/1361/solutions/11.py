n, a = int(input()), list(map(int, input().split()))
i = min((a[i + 2] - a[i], i,) for i in range(n - 2))[1] + 1
a = a[:i] + a[i + 1:]
print(max(a[i + 1] - a[i] for i in range(n - 2)))
