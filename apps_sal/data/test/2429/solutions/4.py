t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        a.append(2 ** (i + 1))
    print(sum(a[:n // 2 - 1]) + a[-1] - sum(a[n // 2 - 1:n - 1]))
