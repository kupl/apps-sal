N = int(input())
L = list(map(int, input().split()))
import copy
U = copy.copy(L)
for i in range (0, N):
	L[i]+=(i+1)
	U[i]= -U[i]+(i+1)


L = sorted(L)
U = sorted(U)

import bisect

count = 0
for i in range (0, N):
	count+= bisect.bisect_right(U, L[i])-bisect.bisect_left(U, L[i])
    
print(count)
