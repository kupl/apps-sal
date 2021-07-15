n,k=map(int,input().split())
s=list(input())
score=0
for i in range(n-1):
  if s[i]==s[i+1]:
    score+=1
print(min(score+2*k,n-1))
