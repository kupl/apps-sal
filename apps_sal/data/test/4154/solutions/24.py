n,m = list(map(int,input().split()))
gate = [[int(i) for i in input().split()] for _ in range(m)]

minv = gate[0][0]
maxv = gate[0][1]

for x in gate:
  minv = max(minv,x[0])
  maxv = min(maxv,x[1])
  
print((maxv-minv+1 if maxv-minv+1 >= 1 else 0))

