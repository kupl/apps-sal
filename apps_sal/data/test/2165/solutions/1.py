def rd():
    return list(map(int, input().split()))


(n, t) = rd()
a = list(rd())
b = list(rd())
x = [[b[i], a[i]] for i in range(n)]
x.sort()
(tot, val) = (sum(a), 0)
for i in range(n):
    val += (t - x[i][0]) * x[i][1]
if val < 0:
    for i in range(n - 1, -1, -1):
        if val - x[i][1] * (t - x[i][0]) >= 0:
            tot -= val / (t - x[i][0])
            val = 0
            break
        tot -= x[i][1]
        val -= (t - x[i][0]) * x[i][1]
if val > 0:
    for i in range(n):
        if val - x[i][1] * (t - x[i][0]) <= 0:
            tot -= val / (t - x[i][0])
            val = 0
            break
        tot -= x[i][1]
        val -= (t - x[i][0]) * x[i][1]
print('%.12f' % tot)
