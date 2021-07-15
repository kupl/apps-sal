Row = int(input())
List = []
for i in range (Row):
  List.append(int(input()))
List.sort(reverse = True)
mid = 0
for i in range(Row):
  mid += List[i]
sumList = [mid]* (Row+1)
for i in range(Row):
  sumList[i] = sumList[i]-List[i]
  if sumList[i] % 10 == 0:
    sumList[i]=0
if sumList[Row] % 10 == 0:
  sumList[Row] = 0
res = max(sumList)
print(res)
