import numpy as np
import bisect as bs
N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

A.sort()
C.sort()
B_a = np.array([bs.bisect_left(A, b) for b in B])
B_c = np.array([N - bs.bisect_right(C, b) for b in B])
ans = np.dot(B_a, B_c)
print(ans)
