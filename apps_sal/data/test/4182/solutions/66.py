n,m,x,y = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if max(max(a),x) < min(min(b),y):
  print("No War")
else:
  print("War")

