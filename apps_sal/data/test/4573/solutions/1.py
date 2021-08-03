import bisect
n = int(input())
x = list(map(int, input().split()))
m = n // 2
y = sorted(x)
for i in range(n):
    if bisect.bisect_right(y, x[i]) > m:
        print(y[m - 1])
    else:
        print(y[m])
