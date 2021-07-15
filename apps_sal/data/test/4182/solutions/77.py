n,m,x,y = map(int,input().split())
xl = list(map(int,input().split()))
yl = list(map(int,input().split()))
z = [i for i in range(x+1,y+1)]
for i in range(len(z)):
  if max(xl) < z[i] <= min(yl):
    print("No War")
    return
print("War")
