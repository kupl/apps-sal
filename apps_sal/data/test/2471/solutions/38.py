H,W,N = map(int,input().split())
D = {}

while N:
  N-=1
  x,y = map(int,input().split())
  
  for i in range(9):
    a = (x+i%3,y+i//3)
    D[a] = D.get(a,0)+(H>=a[0]>2<a[1]<=W)

c = [list(D.values()).count(i+1) for i in range(9)]
print((H-2)*(W-2)-sum(c))

for i in range(9):
    print(c[i])
