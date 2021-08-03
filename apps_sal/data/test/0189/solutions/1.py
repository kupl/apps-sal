n = int(input())
a = [*map(int, input().split())]

mcost = 10**8
ans = 0

for i in range(1, 101):
    tcost = 0
    for j in range(n):
        if a[j] > i:
            d = abs(a[j] - (i + 1))
        elif a[j] < i:
            d = abs(a[j] - (i - 1))
        else:
            d = 0
        tcost += d
    if tcost < mcost:
        mcost, ans = tcost, i

print(ans, mcost)
