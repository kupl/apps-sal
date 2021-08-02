######################################################################
# Write your code here
import sys
input = sys.stdin.readline
#import resource
#resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
# sys.setrecursionlimit(0x100000)
# Write your code here
RI = lambda: [int(x) for x in sys.stdin.readline().strip().split()]
rw = lambda: input().strip().split()
#from collections import defaultdict as df
#import heapq
# heapq.heapify(li) heappush(li,4) heappop(li)
#import random
# random.shuffle(list)
infinite = float('inf')
#######################################################################

t = int(input())

for _ in range(t):
    n, k = RI()
    s = input()

    mini = n

    test = "RGB" * (k // 3 + 5)
    for i in range(n - k + 1):
        count = 0

        for j in range(k):
            if(s[i + j] != test[j]):
                count += 1

        mini = min(count, mini)

    test = "GBR" * (k // 3 + 5)
    for i in range(n - k + 1):
        count = 0

        for j in range(k):
            if(s[i + j] != test[j]):
                count += 1

        mini = min(count, mini)

    test = "BRG" * (k // 3 + 5)
    for i in range(n - k + 1):
        count = 0

        for j in range(k):
            if(s[i + j] != test[j]):
                count += 1

        mini = min(count, mini)

    print(mini)
