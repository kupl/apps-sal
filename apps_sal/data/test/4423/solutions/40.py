n = int(input())

rest = []

for x in range(n):
  a,b = input().split()
  b = int(b)
  rest.append([a,b])
  
  
rest2 = list(sorted(rest, key=lambda x:(x[1]), reverse=True))
rest3 = list(sorted(rest2,key=lambda x:x[0]))

for i in rest3:
  print((rest.index(i)+1))

