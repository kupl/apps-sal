n=int(input())
ar=list(map(int,input().split()))
mn=min(ar)
prev=-float('inf')
ans=float('inf')
for i in range(n):
    if ar[i] == mn:
        ans=min(ans,i-prev)
        prev=i
print(ans)

