n, m, k = map(int, input().split())
x, s = map(int, input().split())
res = n * x
ft = [[0] * 2 for i in range(m)]
st = [[0] * 2 for i in range(k)]
tmparr = list(map(int, input().split()))
for i in range(m):
    ft[i][0] = tmparr[i]
tmparr = list(map(int, input().split()))
for i in range(m):
    ft[i][1] = tmparr[i]
tmparr = list(map(int, input().split()))
for i in range(k):
    st[i][0] = tmparr[i]
tmparr = list(map(int, input().split()))
for i in range(k):
    st[i][1] = tmparr[i]
for i in range(m):
    nows = s - ft[i][1]
    if (nows < 0):
        continue
    nowr = n * ft[i][0]
    if (nows >= st[0][1]):
        l = 0
        r = k
        while r - l > 1:
            m = (l + r) // 2
            if (st[m][1] <= nows):
                l = m
            else:
                r = m
        nowr -= ft[i][0] * st[l][0]
    res = min(res, nowr)
for i in range(k):
    if (st[i][1] <= s):
        res = min(res, x * (n - st[i][0]))
print(res)
