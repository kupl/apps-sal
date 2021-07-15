k,s=map(int,input().split())
cnt=0

for i in range(k+1):
  for j in range(k+1):
    if s-k<=i+j<=s:
      cnt+=1
      
print(cnt)
