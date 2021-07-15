n=int(input())
txy=[list(map(int,input().split())) for i in range(n)]
x,y=0,0
t=0
for i in range(n):
  if abs((x+y) - (txy[i][1]+txy[i][2]))%2 == abs(t-txy[i][0])%2 and abs(t-txy[i][0]) >= abs((x+y)-(txy[i][1]+txy[i][2])):
    x,y=txy[i][1],txy[i][2]
  else:
    print("No")
    return
  t=txy[i][0]
print("Yes")
