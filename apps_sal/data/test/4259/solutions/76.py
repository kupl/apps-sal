K=int(input())
A,B=list(map(int,input().split()))
i=0
can=False
while i<=B:
  i+=K
  if i>=A and i<=B:
    can=True
    break
if can:
  print("OK")
else:
  print("NG")

