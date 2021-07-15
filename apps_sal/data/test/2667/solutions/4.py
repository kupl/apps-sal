N=int(input())
L=list(map(int,input().split()))[:N]
if sum(L)==N*(N+1)/2:
    print("YES")
else:
    print("NO")
