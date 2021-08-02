######################################################################
# Write your code here
import heapq
import sys
import math
input = sys.stdin.readline
#import resource
#resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
# sys.setrecursionlimit(0x100000)
# Write your code here
def RI(): return [int(x) for x in sys.stdin.readline().strip().split()]
def rw(): return input().strip().split()


#from collections import defaultdict as df
# heapq.heapify(li) heappush(li,4) heappop(li)
#import random
# random.shuffle(list)
infinite = float('inf')
#######################################################################


n, k = RI()

l = RI()

l.sort()

i = n // 2
median = l[i]
steps = 0
count = 0
while(i < n):
    temp = l[i]
    while(i < n and l[i] == temp):
        count += 1
        i += 1
    if(i < n):
        a = k // count
        if(a == 0):
            break
        else:
            diff = l[i] - temp
            if(a >= diff):
                k -= (diff * count)
                median = l[i]
                continue
            else:
                k -= (a * count)
                median += a
                break
    else:
        a = k // count
        if(a == 0):
            break
        else:
            median += a
            break
print(median)
