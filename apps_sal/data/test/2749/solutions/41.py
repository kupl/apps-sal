h,w=map(int,input().split());input();a,MAP,w1,h1=list(map(int,input().split())),[[0 for i in range(w)] for j in range(h)],0,0
for i,j in enumerate(a):
  for _ in range(j):
    if w1<w:
      MAP[h1][w1]= i+1
      w1+=1
      if w1==w:
        w1=0
        h1+=1
for i in range(h):
  if i%2!=0: MAP[i]=MAP[i][::-1]
[print(*i,sep=' ') for i in MAP]
