import sys
input = sys.stdin.readline

Q=int(input())
for testcase in range(Q):
    n,k=list(map(int,input().split()))
    A=list(map(int,input().split()))

    if min(A)+k<max(A)-k:
        print(-1)
    else:
        print(min(A)+k)
    

