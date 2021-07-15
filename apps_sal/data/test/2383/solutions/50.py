N=int(input())
List = list(map(int, input().split()))
j = 1
res = 0
for i in range(N):
  if List[i] == j:
    j+=1
  else:
    res += 1
if j == 1:
  res = -1
print(res)
