n, n1, n2 = list(map(int, input().split()))
xs = [int(x) for x in input().split()]

xs.sort()
minn = min(n1, n2)
maxn = max(n1, n2)

mean1 = 0
for i in range(minn):
    mean1 += xs[len(xs) - i - 1]
mean1 /= minn

mean2 = 0
for i in range(maxn):
    mean2 += xs[len(xs) - i - 1 - minn]
mean2 /= maxn

print(mean1 + mean2)
