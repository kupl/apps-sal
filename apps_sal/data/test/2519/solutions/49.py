n,k = map(int,input().split())
p = list(map(int,input().split()))
q = [0]*n
for i in range(n):
  q[i] = (1+p[i])/2
s = [0]*(n+1)
for j in range(n):
  s[j+1]=s[j]+q[j]
t = k+1
answer = s[k]-s[0]
while(t<=n):
  answer = max(answer,s[t]-s[t-k])
  t +=1
print(answer)
