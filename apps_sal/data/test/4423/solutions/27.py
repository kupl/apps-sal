n = int(input())
city = []
l = []
for i in range(n):
  s,p = input().split()
  if s not in city: city.append(s)
  l.append((s, int(p), i+1))
  
city = sorted(set(city))
l = sorted(l, key=lambda x: x[1], reverse=True)
for i in city:
  for j in l:
    if i == j[0]: print(j[2])
