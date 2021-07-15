n=int(input())
A=list(map(int,input().split()))
A.sort()

if sum(A)==2*sum(A[:n]):
    print(-1)
else:
    print(*A)

