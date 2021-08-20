n = int(input())
h = [0] * n
m = [0] * n
for i in range(0, n):
    (h[i], m[i]) = map(int, input().split(':'))
for i in range(0, n):
    for j in range(i, n):
        if h[j] < h[i] or (h[j] == h[i] and m[j] < m[i]):
            t = h[j]
            h[j] = h[i]
            h[i] = t
            t = m[j]
            m[j] = m[i]
            m[i] = t
mxh = 0
mxm = 0
for i in range(0, n):
    if i == n - 1:
        nowh = h[0] + 24 - h[i]
        nowm = m[0] - m[i] - 1
        if nowm < 0:
            nowh = nowh - 1
            nowm = nowm + 60
        if mxh < nowh or (mxh == nowh and mxm < nowm):
            mxh = nowh
            mxm = nowm
    else:
        nowh = h[i + 1] - h[i]
        nowm = m[i + 1] - m[i] - 1
        if nowm < 0:
            nowh = nowh - 1
            nowm = nowm + 60
        if mxh < nowh or (mxh == nowh and mxm < nowm):
            mxh = nowh
            mxm = nowm
print('%02d:%02d' % (mxh, mxm))
