'''
Created on Sep 28, 2014

@author: Ismael
'''

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
s = 0
for i in range(len(A) - 1, -1, -k):
    elems = [A[j] for j in range(i, max(-1, i - k), -1)]
    s += 2 * (max(elems) - 1)
print(s)
