N = int(input())
A = list(map(int,input().split()))
A = [A[i]-(i+1) for i in range(N)]
A = sorted(A)
A.insert(0,0)
if N%2==1:
    b = A[(N+1)//2]
    ans = 0
    for i in range(1,N+1):
        ans += abs(A[i]-b)
else:
    b1 = A[N//2]
    b2 = A[N//2+1]
    bmax = max(b1,b2)
    bmin = min(b1,b2)
    if (bmax-bmin)%2==0:
        b = (bmax+bmin)//2
        ans = 0
        for i in range(1,N+1):
            ans += abs(A[i]-b)
    else:
        b1 = (bmax+bmin)//2
        a1 = 0
        for i in range(1,N+1):
            a1 += abs(A[i]-b1)
        b2 = (bmax+bmin)//2+1
        a2 = 0
        for i in range(1,N+1):
            a2 += abs(A[i]-b2)
        ans = min(a1,a2)
print(ans)
