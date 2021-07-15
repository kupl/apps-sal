N, M = list(map(int,input().split()))

AB = []
for i in range(N):
  A, B = list(map(int,input().split()))
  AB.append([A,B])
AB = sorted(AB,key = lambda x:x[0])
cost = 0

for a,b in AB:
  cost += (min(max(M,0),b))*a
  M-=b
  if M<=0:
    break
print(cost)

