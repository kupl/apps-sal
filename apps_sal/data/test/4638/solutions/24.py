n, c = [int(x) for x in input().split()]
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dpst = [0] * (n + 1)
dplift = [0] * (n + 1)
dpst[2] = a[0]
dplift[2] = c + b[0]
for i in range(3, n + 1):
    dpst[i] = a[i - 2] + min(dpst[i - 1], dplift[i - 1])
    dplift[i] = b[i - 2] + min(c + dpst[i - 1], dplift[i - 1])

for i in range(1, n + 1):
    print(min(dpst[i], dplift[i]), end=" ")
