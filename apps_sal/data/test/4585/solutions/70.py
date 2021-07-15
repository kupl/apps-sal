X=int(input())
SUM=0
for i in range(1,10**6):
  SUM += i
  if SUM >= X:
    print(i)
    return
