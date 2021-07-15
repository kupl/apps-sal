n = int(input())
d = {}
for i in range(n) :
  s = input()
  if s in list(d.keys()) : d[s]+=1
  else : d[s] = 1
print(max(d.values()))

