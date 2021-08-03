n = int(input())
x = list(map(int, input().split()))
xs = sorted(x)
m = (xs[n // 2] + xs[n // 2 - 1]) / 2
for i in range(n):
    if x[i] <= m:
        print(xs[n // 2])
    else:
        print(xs[n // 2 - 1])
