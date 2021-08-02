N, K = map(int, input().split())
A = list(map(int, input().split()))
ind = A.index(1)
n = ind // (K - 1)
if ind % (K - 1):
    n += 1
m = (N - 1 - ind) // (K - 1)
if (N - 1 - ind) % (K - 1):
    m += 1
cmin = n + m
for i in range(max(1, ind + K - N), min(ind, K - 1) + 1):
    n = (ind - i) // (K - 1)
    if (ind - i) % (K - 1):
        n += 1
    m = (N - ind - K + i) // (K - 1)
    if (N - ind - K + i) % (K - 1):
        m += 1
    cnt = n + m + 1
    cmin = min(cmin, cnt)
print(cmin)
