lm = [0] * 200000
li = [0] * 200000
rm = [0] * 200000
ri = [0] * 200000
(n, k) = list(map(int, input().split()))
d = list(map(int, input().split()))
sm = 0
for i in range(k):
    sm += d[i]
lm[k - 1] = sm
li[i - 1] = 0
for i in range(k, n):
    sm = sm - d[i - k] + d[i]
    if sm > lm[i - 1]:
        lm[i] = sm
        li[i] = i - k + 1
    else:
        lm[i] = lm[i - 1]
        li[i] = li[i - 1]
sm = 0
for i in range(n - 1, n - 1 - k, -1):
    sm += d[i]
rm[n - k] = sm
ri[n - k] = n - k
for i in range(n - k - 1, -1, -1):
    sm = sm - d[i + k] + d[i]
    if sm >= rm[i + 1]:
        rm[i] = sm
        ri[i] = i
    else:
        rm[i] = rm[i + 1]
        ri[i] = ri[i + 1]
mx = -1
for i in range(k - 1, n - k):
    if lm[i] + rm[i + 1] > mx:
        mx = lm[i] + rm[i + 1]
        a = li[i]
        b = ri[i + 1]
print(a + 1, b + 1)
