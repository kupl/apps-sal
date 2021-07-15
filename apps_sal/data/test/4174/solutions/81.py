N,X = map(int,input().split())
L = list(map(int,input().split()))

D = []
D.append(0)

for i in range(0,N):
  D.append(D[i]+L[i])

cnt = 0
for d in D:
  if d <= X:
    cnt += 1
    
print(cnt)
