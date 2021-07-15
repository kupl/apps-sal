n=int(input())
a,b=[],[]
for i in range(n):
  x,y=list(map(int,input().split()))
  a.append(x+y)
  b.append(x-y)
print((max(max(a)-min(a),max(b)-min(b))))

