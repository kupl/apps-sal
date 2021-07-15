n=int(input())
l=list(map(int,input().split()))
if 1 not in l:
  print(-1)
else:
  i=0
  j=1
  cnt=0
  while i<n:
    if l[i]==j:
      j+=1
    else:
      cnt+=1
    i+=1
  print(cnt)
