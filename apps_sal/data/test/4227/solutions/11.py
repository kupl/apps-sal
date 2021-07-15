def dfs(place,number,checkedList,path):
  checkedList[place] = 1
  if sum(checked) == number:
    return 1
  pathNumber = 0
  for i in path[place]:
    if checkedList[i] == 1:
      continue
    pathNumber += dfs(i,number,checkedList,path)
    checkedList[i] = 0
  return pathNumber  

n, m = map(int, input().split())

checked = [0] * 8
path = [ [] for _ in range(8)]
for i in range(m):
  a, b = map(int, input().split())
  path[a-1].append(b-1)
  path[b-1].append(a-1)
  #print(path)
  
print(dfs(0,n,checked,path))
