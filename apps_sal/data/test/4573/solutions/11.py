import statistics

n = int(input())
x = list(map(int, input().split()))
xmd = statistics.median(x)
xs = sorted(x)
for i in x:
    if i < xmd:
        print((xs[n // 2]))
    else:
        print((xs[n // 2 - 1]))
