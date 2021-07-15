n = int(input())

cl = list(map(int, input().split()))

pos = {}
color = 0
res = []

for x in cl:
  if x in pos.keys():
    if pos[x][0]!=0:
      res.append(pos[x][1])
      pos[x][0]-=1
    else:
      color+=1
      res.append(color)
      pos[x] = [n-x-1, color]
  else:
    color+=1
    res.append(color)
    pos.update({x:[n-x-1, color]})

for x in pos.keys():
  if pos[x][0]!=0:
    print("Impossible")
    return

print("Possible")
print(*res)
