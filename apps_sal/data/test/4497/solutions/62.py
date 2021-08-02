import sys
import bisect
n = int(input())
li = [2, 4, 8, 16, 32, 64]
index = bisect.bisect(li, n) - 1
if index == -1:
    print(n)
    return
print(li[index])
