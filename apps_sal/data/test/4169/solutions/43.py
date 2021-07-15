N,M=map(int,input().split())
List = []
for i in range (N):
  List.append(list(map(int, input().split())))
List.sort()
res = 0
num = 0
i = 0
while num < M:
  if List[i][1] != 0:
    pass
  else:
    i +=1
  num += 1
  res += List[i][0]
  List[i][1] += -1
print(res)
