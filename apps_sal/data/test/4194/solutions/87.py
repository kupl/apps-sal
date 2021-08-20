(n, m) = map(int, input().split(' '))
alist = list(map(int, input().split(' ')))
asum = sum(alist)
if n - asum >= 0:
    print(n - asum)
else:
    print(-1)
