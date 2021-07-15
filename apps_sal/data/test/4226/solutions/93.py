X,Y=map(int,input().split())

for cnt in range(X+1):
  if 2*cnt + 4*(X-cnt) == Y:
    print('Yes')
    break
else:
  print('No')
