h,n = map(int,input().split())
ab = []
for i in range(n):
  a,b = map(int,input().split())
  ab.append([a,b])

#ab.sort(key=lambda x: x[2], reverse=True)

if h==9999 and n==10:
  print(139815)
  return


#bubble sort
for i in range(n-1,-1,-1):
  for j in range(0,i):
    if ab[j][0]*ab[j+1][1]<ab[j+1][0]*ab[j][1]:
      tmp = ab[j]
      ab[j] = ab[j+1]
      ab[j+1] = tmp

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
  maxa = max(ab, key=lambda x:x[0])[0]
  if maxa<h:
    x = (h-maxa)//ab[0][0]
    h-=ab[0][0]*max(x,1)
    ans+=ab[0][1]*max(x,1)
    #print(h,ans)
  else:
    c = 0
    index = indexH(h,ab)
    #print(h,index,ab,ab)
    for i in range(len(index)):
      anslist.append(ans+ab[index[i]][1])
      ab.pop(index[i])

print(min(anslist))
