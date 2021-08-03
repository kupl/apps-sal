n, c = map(int, input().split())
walk = list(map(int, input().split()))
lift = list(map(int, input().split()))
dpl = [0] * n
dpw = [0] * n
dpl[0] = c
print(0, end=" ")
for i in range(1, n):
    dpl[i] = min(dpw[i - 1] + c, dpl[i - 1]) + lift[i - 1]
    dpw[i] = min(dpw[i - 1], dpl[i - 1]) + walk[i - 1]
    print(min(dpl[i], dpw[i]), end=" ")
