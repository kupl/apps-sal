N,M = list(map(int,input().split()))
d = {i:0 for i in range(1,M+1)}

for _ in range(N):
  L = list(map(int,input().split()))[1:]
  for i in L:
    d[i] += 1
    
cnt = sum([1 for k,v in list(d.items()) if v == N])
print(cnt)

