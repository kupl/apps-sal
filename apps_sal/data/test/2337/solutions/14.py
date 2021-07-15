'''
Created on Jun 4, 2014

@author: Nathaniel
'''

import bisect

def nexti():
    return list(map(int, input().split()))
def nextl():
    return list(map(int, input().split()))

n, m = nexti()
a = sorted(nextl())
b = sorted(nextl())
count = 0
i=0
j=0
n = len(a)

while i < n:
    bis = bisect.bisect_left(b, a[i])
    if bis != len(b):
        count+=1
        del b[bis]
    i+=1
print(n - count)
        


