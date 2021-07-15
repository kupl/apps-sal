N = int(input())
locs = []
S = 0

for _ in range(N):
  locs.append(list(map(int,input().split())))
  
for i in range(N):
  for j in range(i+1,N):
    dis = ((locs[i][0]-locs[j][0])**2 + (locs[i][1]-locs[j][1])**2)**(1/2)
    S += dis

print(2*S/N)
