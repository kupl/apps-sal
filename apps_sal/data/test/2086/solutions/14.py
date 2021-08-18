
n = int(input())
n = n * 2
a = list(map(int, input().split()))
a = a + a
s, f = list(map(int, input().split()))
sum = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    sum[i] = sum[i - 1] + a[i - 1]
ran = f - s
msum, idx = 0, 0
bb = int(1e18)
for i in range(ran, n + 1):
    if sum[i] - sum[i - ran] > msum:
        msum = sum[i] - sum[i - ran]
        idx = i - ran + 1
        if idx < s:
            idx = s - idx + 1
        elif idx > s:
            idx = 1 - abs(s - idx)
            idx += n
        else:
            idx = 1
        idx = idx % (int(n / 2))
        if (idx == 0):
            idx = int(n / 2)
        bb = idx
    elif sum[i] - sum[i - ran] == msum:
        idx = i - ran + 1
        if idx < s:
            idx = s - idx + 1
        elif idx > s:
            idx = 1 - abs(s - idx)
            idx += n
        else:
            idx = 1
        idx = idx % (int(n / 2))
        if (idx == 0):
            idx = int(n / 2)
        if idx < bb:
            bb = idx
            msum = sum[i] - sum[i - ran]


print(bb)
