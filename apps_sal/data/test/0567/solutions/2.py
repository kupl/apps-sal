n = int(input())
a = list(map(int, input().split()))
maxd = 0
for i in range(n):
    if a[i] <= 500000:
        maxd = max(maxd, a[i] - 1)
    else:
        maxd = max(maxd, 1000000 - a[i])
print(maxd)
