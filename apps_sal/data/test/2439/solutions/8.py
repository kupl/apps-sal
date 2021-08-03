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
    M = sum(A)
    if M == 0:
        print('NO')
    elif M > 0:
        A.sort(reverse=True)
        print('YES')
        print(*A)
    else:
        A.sort()
        print('YES')
        print(*A)
