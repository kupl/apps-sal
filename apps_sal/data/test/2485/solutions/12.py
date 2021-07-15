h,w,m = map(int,input().split())
t = [tuple(map(lambda x:int(x)-1,input().split())) for _ in range(m)] 
ht = [0]*h
wt = [0]*w
for y,x in t:
  ht[y] += 1
  wt[x] += 1
htm = max(ht)
wtm = max(wt)
htt = [i for i in range(h) if ht[i]==htm]
wtt = [i for i in range(w) if wt[i]==wtm]
ans = htm+wtm-1
t = set(t)
for i in htt:
  for j in wtt:
    if (i,j) not in t:
      print(htm+wtm)
      return
print(htm+wtm-1)
