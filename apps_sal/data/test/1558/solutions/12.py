(n, r, avg) = [int(i) for i in input().split()]
a = [0] * n
b = [[0] * 2 for i in range(n)]
for j in range(n):
    (a[j], b[j][0]) = [int(i) for i in input().split()]
    b[j][1] = j
b.sort()
mid = -1
sum1 = sum(a)
res = 0
hod = 0
sumOLD = 0
if sum1 / n < avg:
    while mid < avg:
        sumOLD = sum1
        sum1 += min(r - a[b[hod][1]], avg * n - sumOLD)
        res += b[hod][0] * min(r - a[b[hod][1]], avg * n - sumOLD)
        hod += 1
        mid = sum1 / n
    print(res)
else:
    print(0)
