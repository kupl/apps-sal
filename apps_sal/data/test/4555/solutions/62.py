a,b,k = list(map(int,input().split()))
l = []
for i in range(a,min(b,a+k)):
  l.append(i)
for i in range(max(b-k+1,a),b+1):
  l.append(i)
ans = sorted(set(l))
for i in ans:
  print(i)


