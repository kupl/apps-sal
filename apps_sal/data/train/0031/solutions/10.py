# alpha = "abcdefghijklmnopqrstuvwxyz"
# prime = 1000000007#998244353
# INF = 10000

# from sys import stdout
# from heapq import heappush, heappop
# from collections import defaultdict
# from collections import deque
# import bisect

# from math import sqrt
# from math import gcd
# from math import log2

# with open('input.in','r') as Reader:
#     with open('output.out','w') as out:
# n = int(Reader.readline())


# print(len(arr))
# print(arr[:10])


t = int(input())
for test in range(t):
    # n = int(input())
    # n, m = list(map(int, input().split()))
    # n2, m2 = list(map(int, input().split()))
    s = input()
    v = set()
    start = 0
    ans = 0
    cur = [0, 0, 0, 0]
    for i in s:
        if i == "N":
            cur[2] += 1
        elif i == "S":
            cur[2] -= 1
        elif i == "E":
            cur[3] += 1
        else:
            cur[3] -= 1

        key1 = str(cur)
        key2 = str([cur[2], cur[3], cur[0], cur[1]])
        if key1 in v:
            ans += 1
        else:
            ans += 5

        v.add(key1)
        v.add(key2)

        cur[0] = cur[2]
        cur[1] = cur[3]
    print(ans)
