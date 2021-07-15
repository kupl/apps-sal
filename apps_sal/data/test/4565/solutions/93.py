n=int(input())
s=input()
data=[0]*(n+1)
for i in range(n):
  if s[i]=='E':
    data[i+1]=data[i]+1
  else:
    data[i+1]=data[i]
print(min(i-data[i]+data[n]-data[i+1] for i in range(n)))
