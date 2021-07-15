N = int(input())
dic = {}
for _ in range(N):
  S = input()
  if S in dic:
    dic[S] += 1
  else:
    dic[S] = 1

lst = []
M = max(dic.values())
for k in dic.keys():
  if dic[k] == M:
    lst.append(k)

lst.sort()

for i in range(len(lst)):
  print(lst[i])
