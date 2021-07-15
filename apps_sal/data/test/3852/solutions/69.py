n = int(input())
lis = list(map(int,input().split()))
AngeKatrina = 0
LizeHelesta = 0
for i,InuiToko in list(enumerate(lis)):
  if InuiToko >= 0:
    if InuiToko >= AngeKatrina:
      AngeKatrina = InuiToko
      AngeSoko = i+1
  else:
    if -InuiToko >= LizeHelesta:
      LizeHelesta = -InuiToko
      LizeHiyoko = i+1
print(2*n-1)
if AngeKatrina >= LizeHelesta:
  for i in range(1,n+1):
    print(AngeSoko,i)
  for i in range(1,n):
    print(i,i+1)
else:
  for i in range(1,n+1):
    print(LizeHiyoko,i)
  for i in range(n,1,-1):
    print(i,i-1)
