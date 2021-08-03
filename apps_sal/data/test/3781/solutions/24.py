import sys
import os
import io
input = sys.stdin.readline
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
T = int(input())
ans = [0] * T
for t in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if n % 2 == 0:
        ans[t] = 'Second'
        for i in range(0, n, 2):
            if A[i] != A[i + 1]:
                ans[t] = 'First'
                break
    else:
        ans[t] = 'Second'
print(*ans, sep='\n')
