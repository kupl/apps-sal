from math import ceil, log
from heapq import heappop, heappush, heapify
t = 1
for test in range(t):
    (n, k) = list(map(int, input().split()))
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    arr = [i for i in sorted(enumerate(p), key=lambda x: x[1])]
    maxcoins = [0 for i in range(k)]
    heapify(maxcoins)
    ans = list(p)
    tmpSum = 0
    tmpSum2 = 0
    prev = arr[0][1]
    for (ind, power) in arr:
        if power > prev:
            ans[ind] = tmpSum + c[ind]
            tmpSum2 = tmpSum
        else:
            ans[ind] = tmpSum2 + c[ind]
        heappush(maxcoins, c[ind])
        tmpSum += c[ind]
        tmpSum -= heappop(maxcoins)
    print(*ans)
