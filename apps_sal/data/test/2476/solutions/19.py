# F - Distinct Numbers
from bisect import bisect_left

def isOK(c, k, N, L, cum_sum):
    i = bisect_left(L, c)
    s = c * (N - i) + cum_sum[i];
    return (s >= c * k)

N = int(input())
D = list(map(int, input().split()))
freq = [0] * N
for d in D:
    freq[d - 1] += 1
    
freq.sort()
cum_sum = [0] * (N + 1)
for i in range(N):
    cum_sum[i + 1] = cum_sum[i] + freq[i]
    
for k in range(1, N + 1):
    l = 0
    r = int(N / k) + 1
    while l + 1 < r:
        c = int((l + r) / 2)
        ok = isOK(c, k, N, freq, cum_sum)
        if ok:
            l = c
        else:
            r = c
    print(l)

