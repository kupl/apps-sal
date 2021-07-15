from collections import deque
from math import *
n, k ,q = list(map(int, input().split()))
A = []
lens = 0
B = list(map(int, input().split()))
for i in range(q):
    per1,per2 = list(map(int, input().split()))
    if per1 == 1:
        if lens < k:
            A.append([per2, B[per2-1]])
            lens += 1
        else:
            c = float('infinity')
            r = 0
            for i in range(k):
                if A[i][1] < c:
                    c = A[i][1]
                    r = i
            if B[per2 -1] > A[r][1]:
                
                A[r] = [per2, B[per2-1]]
    else:
        si = True
        for i in range(lens):
            if A[i][0] == per2:
                si = False
                break
        if si:
            print('NO')
        else:
            print('YES')

