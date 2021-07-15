n,k = map(int,input().split())
lst = list(map(int,input().split()))
E = [0]
for x in lst:
  E.append((1+x)/2+E[-1])
s = 0
for i in range(n+1-k):
  if s < E[i+k] - E[i]:
    s = E[i+k] - E[i]
print(s)    
