'''from collections import Counter,defaultdict,deque

from math import factorial as fact
import math'''

t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    ans = []
    ans.append(arr[0])
    p1 = 1
    p2 = n - 1
    while p2 >= p1:
        if abs(ans[-1] - arr[p1]) > abs(ans[-1] - arr[p2]):
            ans.append(arr[p1])
            p1 += 1
        else:
            ans.append(arr[p2])
            p2 -= 1
    ans.reverse()
    print(*ans)
