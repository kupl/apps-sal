import sys
input = sys.stdin.readline
def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = [int(input()) for i in range(N-1)]

    def mex(x,y):
        if x+y==1: return 2
        if x==0 or y==0: return 1
        return 0

    n = min(4,N)
    arr = [[-1]*n for _ in range(n)]
    for i,a in enumerate(A):
        if i>=4: break
        arr[0][i] = a
    for i,b in enumerate(B):
        if i+1>=4: break
        arr[i+1][0] = b
    for i in range(1,n):
        for j in range(1,n):
            arr[i][j] = mex(arr[i-1][j], arr[i][j-1])

    ctr = [0,0,0]
    for i in range(n):
        for j in range(n):
            ctr[arr[i][j]] += 1
    if N <= 4:
        print(*ctr)
        return

    arrtop = [[-1]*(N-3) for _ in range(4)]
    for i in range(4):
        arrtop[i][0] = arr[i][-1]
    for j in range(4,N):
        arrtop[0][j-3] = A[j]
    for i in range(1,4):
        for j in range(1,N-3):
            arrtop[i][j] = mex(arrtop[i-1][j], arrtop[i][j-1])
            ctr[arrtop[i][j]] += (1 if i<3 else N-3-j)
    for a in A[4:]:
        ctr[a] += 1

    arrleft = [[-1]*4 for _ in range(N-3)]
    for j in range(4):
        arrleft[0][j] = arr[-1][j]
    for i in range(4,N):
        arrleft[i-3][0] = B[i-1]
    for i in range(1,N-3):
        for j in range(1,4):
            arrleft[i][j] = mex(arrleft[i-1][j], arrleft[i][j-1])
            ctr[arrleft[i][j]] += (1 if j<3 else N-3-i)
    for b in B[3:]:
        ctr[b] += 1

    ctr[arr[-1][-1]] += N-4
    print(*ctr)

solve()
