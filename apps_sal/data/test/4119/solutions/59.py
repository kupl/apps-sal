(n, m) = list(map(int, input().split()))
x = list(map(int, input().split()))
x.sort()
total = max(x) - min(x)
if n >= m:
    print(0)
elif n == 1:
    print(total)
else:
    gap = []
    for (i, j) in zip(x, x[1:]):
        gap.append(j - i)
    gap.sort(reverse=True)
    print(total - sum(gap[:n - 1]))
