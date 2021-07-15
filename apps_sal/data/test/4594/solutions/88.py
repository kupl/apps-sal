N = int(input())
d = []
for i in range(N):
  d.append(int(input()))

num = [0]*(max(d)+1)
for i in range(N):
  num[d[i]] +=1

res = 0

for i in range(max(d)+1):
  if num[i]:
    res += 1

print(res)
