# レベルLのN番目
def solve(L,N):
    if L == 0:
        return 1
    if N == 1:
        return 0
    elif N <= 2**(L+1)-2:
        return solve(L-1,N-1)
    elif N == int(2**(L+1)-1):
        return 2**L
    return solve(L-1,N-2**(L+1)+1)+2**L
    

N,X = map(int,input().split())
print(solve(N,X))
