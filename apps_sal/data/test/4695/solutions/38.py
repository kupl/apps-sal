a,b = [int(x) for x in input().split()]
g = [[] for x in range(3)]
g[0] = [1,3,5,7,8,10,12]
g[1] = [4,6,9,11]
g[2] = [2]
res = "No"
for i in range(3):
  if a in g[i] and b in g[i]:
    res = "Yes"
    
print(res)
