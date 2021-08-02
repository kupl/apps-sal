import heapq as hq
import itertools
import math
import collections
ma = lambda: map(int, input().split())
lma = lambda: list(map(int, input().split()))
ni = lambda: int(input())
yn = lambda fl: print("Yes") if fl else print("No")

abc = lma()
abc.sort()
b = abc[2] - abc[0]
c = abc[2] - abc[1]
if b % 2 == 0 and c % 2 == 0:
    ans = b // 2 + c // 2
elif b % 2 == 1 and c % 2 == 1:
    ans = (b - 1) // 2 + (c - 1) // 2 + 1
else:
    ans = b // 2 + c // 2 + 2
print(ans)
