
n, c = list(map(int, input().split()))

lis = []

a = list(map(int, input().split()))
b = list(map(int, input().split()))

asum = 0
bsum = c

for i in range(n):

    lis.append(min(asum, bsum))

    if i == n - 1:
        break

    oasum = asum

    asum = min(asum + a[i], bsum + a[i])

    bsum = min(oasum + b[i] + c, bsum + b[i])

print(" ".join(map(str, lis)))
