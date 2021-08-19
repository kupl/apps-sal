def MII(): return map(int, input().split())


n, k = MII()
count = 0
# x=a+b,y=c+d
for x in range(2, 2 * n + 1):
    y = x - k
    if 2 <= y <= 2 * n:
        abmax = min(x - 1, n)
        abmin = x - abmax
        cdmax = min(y - 1, n)
        cdmin = y - cdmax
        count += (abmax - abmin + 1) * (cdmax - cdmin + 1)
print(count)
