n=int(input())
m=[list(map(str,input().split())) for i in range(n)]

cnt=0

for i in range(n):
  m[i][0]=float(m[i][0])
  if m[i][1]=='BTC':
    m[i][0]*=380000.0
  cnt+=m[i][0]

print(cnt)
