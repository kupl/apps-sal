N = int(input())
l = [[] for i in range(N)]
li = []
for i in range(N-1):
  a, b = map(int, input().split())
  l[a-1].append(b-1)
  li.append([a-1, b-1])
  
ans = [-1] * N

for i in range(N):
  x = 0
  for j, h in enumerate(l[i]):
    if ans[i] == j:
      x += 1
    ans[h] = j+x
    
print(max(ans)+1)
for i in range(N-1):
  print(ans[li[i][1]]+1)
