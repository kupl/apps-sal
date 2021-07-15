import bisect
n,m = list(map(int,input().split()))
A = list(map(int,input().split()))
A.sort()
S = [0]*(n+1)
for i in range(n):
    S[i+1] = S[i] + A[i]

def cnt(x,A,S):
    res = 0
    for i,a in enumerate(A):
        res += bisect.bisect_left(A,x - a)
    return res

def ans(x,A,S):
    res = 0
    for i,a in enumerate(A):
        res += a*bisect.bisect_left(A,x-a) + S[bisect.bisect_left(A,x-a)]
    return res

top = A[-1]*2+1
bottom = 0
# mid以上が何個あるか
while top - bottom > 1:
    mid = (top + bottom)//2
    if n*n - cnt(mid,A,S) > m:
        bottom = mid
    else:
        top = mid

print((S[-1]*2*n - ans(top,A,S) + bottom*(m - (n*n - cnt(top,A,S)))))

