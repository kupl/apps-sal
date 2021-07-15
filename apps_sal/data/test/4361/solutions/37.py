n,k=map(int,input().split())
h=[int(input()) for i in range(n)]
h.sort(reverse=True)
ans=float('inf')
for i in range(n-k+1):
  ans=min(h[i]-h[i+k-1],ans)
print(ans)
