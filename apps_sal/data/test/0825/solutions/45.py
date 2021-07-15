N = int(input())
M = N
pf = []
K = 2

while K*K <= M:
  while N%K == 0:
    pf.append(K)
    N = N//K
  K += 1
  
if N != 1:
  pf.append(N)

ans = 0

for i in set(pf):
  C = pf.count(i)
  for j in range(20):
    if j*(j+1)//2 <= C < (j+1)*(j+2)//2:
      ans += j
  
print(ans)
