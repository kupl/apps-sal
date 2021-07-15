n,m=[int(i) for i in input().strip().split()]
c=[int(i) for i in input().strip().split()]
t=[int(i) for i in input().strip().split()]

ci=0
ti=0
ans=0

while ci<n:
  if ti==m-1:
    ans=max(ans,abs(t[-1]-c[ci]),abs(t[-1]-c[-1]))
    break
  while ti<=m-2:
    if abs(t[ti]-c[ci])>=abs(t[ti+1]-c[ci]):
      ti+=1
    else:
      break
  ans=max(ans,abs(t[ti]-c[ci]))
  ci+=1
print(ans)

