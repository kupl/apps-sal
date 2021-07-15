N = int(input())
Ns = []
for i in range(N):
  Ns.append(input())
  
M = int(input())
Ms = []
for i in range(M):
  Ms.append(input())
  
Ws = list(set(Ns + Ms))

As = []
for i in Ws:
  ans = 0
  for j in Ns:
    if i == j:
      ans += 1
  for j in Ms:
    if i == j:
      ans -= 1
  As.append(ans)
  
print((max(max(As), 0)))

