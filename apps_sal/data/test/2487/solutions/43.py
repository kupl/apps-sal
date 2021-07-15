n = int(input())
tree = [[] for _ in range(n)]
for i in range(n-1):
  v, w = map(int, input().split())
  if v > w:
    v, w = w, v
  tree[w-1].append(v-1)
  
ans = 0
count = 0
for i in range(n):
  count += i+1
  for v in tree[i]:
    count -= v+1 
  ans += count
  
print(ans)
