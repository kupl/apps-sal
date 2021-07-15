import collections

N=int(input())
List = list(map(int, input().split()))
sumList = []
for i in range(N):
  sumList.append(List[i])
  sumList.append(List[i]+1)
  sumList.append(List[i]-1)
c = collections.Counter(sumList)
print(c.most_common()[0][1])
