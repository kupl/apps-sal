N = int(input())
count = [1 for _ in range(N+2)]
count[-1] = 0
count[0] = 0
nextpoint = [[] for _ in range(N+1)]
for _ in range(N-1):
  u, v = list(map(int, input().split()))
  if u > v:
    nextpoint[v].append(u)
  else:
    nextpoint[u].append(v)



#print(nextpoint)
for k in range(1, N):
  for item in nextpoint[k]:
    count[item] -= 1

#print(count)
ans = 0
for k in range(1, N):
  count[k+1] += count[k]
#print(count)
ans = sum(count) #L=1
#print(ans)
before = ans
for k in range(1, N):#L=2~N
  before -= N-k+1
  for item in nextpoint[k]:
    before += N+1-item
  ans += before
print(ans)


