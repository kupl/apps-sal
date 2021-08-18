"""
Created on Wed Oct 16 20:35:46 2013

@author: Praveen Kumar
"""
import sys

x, n = list(map(int, input().split()))
d = {}
for i in range(n):
    a = list(map(int, input().split()))
    b = [1, 2, 3]
    rf = bf = wf = 0
    for j in a:
        if j in d:
            b.remove(d[j])
            a.remove(j)
    if len(b) != 0:
        for j in range(len(a)):
            d[a[j]] = b[j]

for i in range(1, len(d) + 1):
    sys.stdout.write(str(d[i]) + " ")
