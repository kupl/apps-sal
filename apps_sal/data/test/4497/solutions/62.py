n = int(input())
li = [2,4,8,16,32,64]
import bisect
index = bisect.bisect(li,n)-1
import sys
if index == -1:
    print(n)
    return
print(li[index])
