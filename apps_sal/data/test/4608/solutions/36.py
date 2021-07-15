N=int(input())
a=[None]+[int(input()) for i in range(N)]
c=1

for i in range(1, N+1):
  if a[c]==2:
    print(i)
    return
  else:
    c=a[c]+0
    
print(-1)
