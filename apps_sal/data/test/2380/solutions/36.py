import bisect
import numpy as np

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A = np.array(A, dtype=np.int64)

lst = [list(map(int, input().split())) for _ in range(M)]
lst = sorted(lst, key=lambda x: x[1], reverse=True)

x = 0
for i in range(len(lst)):
    idx = bisect.bisect_left(A[x:], lst[i][1])

    if(A[x + idx - 1] <= lst[i][1]):
        if(lst[i][0] >= idx):
            A[x:(x + idx)] = lst[i][1]
            x = x + idx
        else:
            A[x:(x + lst[i][0])] = lst[i][1]
            x = x + lst[i][0]
    else:
        break

print(sum(A))
