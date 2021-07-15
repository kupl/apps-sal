import sys

n = int(input())
A = sorted(list(map(int,input().split())))
ans = 1

if A[0] == 0:
    print((0))
else:
    for i in range(len(A)):
        ans *= A[i]
        if ans > 10**18:
            print((-1))
            return
    print(ans)

