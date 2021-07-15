N = int(input())
List = []
for i in range (2):
  List.append(list(map(int, input().split())))
sumList1 = [0]*N
sumList2 = [0]*N
for i in range(N):
  if i == 0:
    sumList1[i] = List[0][i]
    sumList2[N-1-i] = List[1][N-1-i]
  else:
    sumList1[i] = List[0][i]+sumList1[i-1]
    sumList2[N-1-i] = List[1][N-1-i]+sumList2[N-i]
res = 0
for i in range(N):
  res = max(sumList1[i]+sumList2[i],res)
print(res)
