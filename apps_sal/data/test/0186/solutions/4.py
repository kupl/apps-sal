n, m = list(map(int, input().split()))
maxn = 0
for i in range(n):
    maxn += 2
    if maxn % 3 == 0:
        maxn += 2
maxm = m * 6 - 3
now = 6
while now < max(maxm, maxn):
    if maxm >= maxn:
        maxm -= 3
        if maxm % 2 == 0 and maxm - 3 > now:
            maxm -= 3
    else:
        maxn -= 2
        if maxn % 3 == 0 and maxn - 2 > now:
            maxn -= 2
    now += 6
print(max(maxm, maxn))
