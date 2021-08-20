(n, k) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
c = list(range(1, n + 1))
ved = 0
for i in a:
    n = i % len(c)
    ved = ved + n
    if ved >= len(c):
        ved -= len(c)
    print(c[ved], end=' ')
    c.pop(ved)
