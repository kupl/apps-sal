# alpha = "abcdefghijklmnopqrstuvwxyz"
# prime = 998244353
# INF = 1000000000000000000000

# from sys import stdout
# from heapq import heappush, heappop
from collections import defaultdict
# from collections import deque

# from math import sqrt
# from math import gcd
# from math import log2

t = 1  # int(input())

for test in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    D = defaultdict(int)
    ind1 = 0
    ind2 = -1
    for i in a:
        D[i] += 1
    count = 0
    seta = list(set(a))
    for i in seta:
        if D[i] > 1:
            count += 1
    if count == 0:
        print(0)
        return
    tmp_count = 0
    ans = n
    while True:
        # print("check", tmp_count, count, ind2)
        if tmp_count < count:
            ind2 += 1
            if ind2 == n:
                break
            D[a[ind2]] -= 1
            if D[a[ind2]] == 1:
                tmp_count += 1
        elif tmp_count == count:
            ans = min(ind2 - ind1 + 1, ans)
            D[a[ind1]] += 1
            if D[a[ind1]] == 2:
                tmp_count -= 1
            ind1 += 1
    print(ans)
