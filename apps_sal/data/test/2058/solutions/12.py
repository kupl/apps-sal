def read(): return list(map(int, input()))


a, b = read(), read()
n, m = len(a), len(b)
cnt1 = [0] * (n + 1)
cnt0 = [0] * (n + 1)
if a[0]:
    cnt1[0] = 1
else:
    cnt0[0] = 1
for i in range(1, n):
    cnt1[i] = cnt1[i - 1]
    cnt0[i] = cnt0[i - 1]
    if a[i]:
        cnt1[i] += 1
    else:
        cnt0[i] += 1
Sum = 0
for i in range(m):
    L = max(0, n + i - m)
    R = min(n - 1, i)
    if b[i]:
        cur = cnt0[R] - cnt0[L - 1]
    else:
        cur = cnt1[R] - cnt1[L - 1]
    Sum += cur
print(Sum)
