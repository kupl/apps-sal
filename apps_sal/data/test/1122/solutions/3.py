n,m=map(int,input().split())
#1とnがつながっているときのa,bの最短距離
def dist(a,b):
  return min(abs(a-b),n-abs(a-b))

a,b = n,1
S=set()
for i in range(m):
  distab = dist(a,b)
  #distabがnの半分のとき
  if 2*distab == n or distab in S:
    a -= 1
  print(a,b)
  S.add(distab)
  a -= 1
  b += 1
