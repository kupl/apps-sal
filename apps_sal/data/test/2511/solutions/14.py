n, k = list(map(int, input().split()))
mod = 10**9+7
data = [[] for j in range(n+1)]
done = [0]*(n+1)
colors = [k-1]*(n+1)

for i in range(n-1):
  a, b = list(map(int, input().split()))
  data[min(a,b)].append(max(a,b))
  data[max(a,b)].append(min(a,b))

queue = [1]
ans = 1
colors[1] += 1
for d in data[1]:
  colors[d] += 1
while queue != []:
  idx = queue.pop(0)
  done[idx] = 1
  ans *= colors[idx]
  ans %= mod
  cnt = 0
  for i in range(len(data[idx])):
    if done[data[idx][i]]:
      continue
    cnt += 1
    colors[data[idx][i]] -= cnt
    queue.append(data[idx][i])

print(ans)
  

