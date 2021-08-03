from math import log10
N = int(input())
l = list(map(int, input().split()))
l.sort()
x = round(pow(10, log10(l[-1]) / (N - 1)))
minm = pow(10, 15)
for b in range(max(1, x - 3), x + 2):
    n = 0
    for i in range(N):
        n += abs(pow(b, i) - l[i])
    minm = min(minm, n)
print(minm)
