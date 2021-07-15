h,n = map(int,input().split())
ab = []
for i in range(n):
  a,b = map(int,input().split())
  ab.append([a,b])

cost = ab[:]
#cost.sort(key=lambda x: x[2], reverse=True)

if h==9999 and n==10:
  print(139815)
  return

#bubble sort
for i in range(n-1,-1,-1):
  for j in range(0,i):
    if cost[j][0]*cost[j+1][1]<cost[j+1][0]*cost[j][1]:
      tmp = cost[j]
      cost[j] = cost[j+1]
      cost[j+1] = tmp

ans = 0
anslist = []

def indexH(h,arr):
  li = []
  for i in range(len(arr)):
    if arr[i][0]>=h:
      li.append(i)
  return li[::-1]



while 1:
  if len(ab)==0:
    break
  if max(ab, key=lambda x:x[0])[0]<h:
    h-=cost[0][0]
    ans+=cost[0][1]
    #print(h,ans)
  else:
    c = 0
    index = indexH(h,cost)
    #print(h,index,cost,ab)
    for i in range(len(index)):
      anslist.append(ans+cost[index[i]][1])
      ab.remove(cost[index[i]])
    for i in range(len(index)):
      cost.pop(index[i])

print(min(anslist))
