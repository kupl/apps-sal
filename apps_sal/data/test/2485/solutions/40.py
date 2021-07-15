H,W,M=map(int,input().split())
h=[0]*(H+1)
w=[0]*(W+1)
hw=[0]*M
for i in range(M):
  y,x=map(int,input().split())
  hw[i]=(y,x)
  h[y]+=1
  w[x]+=1
cnt=0
mxh=max(h)
mxw=max(w)
for hi,wi in hw:
  if h[hi]==mxh and w[wi]==mxw:
    cnt+=1
if h.count(mxh)*w.count(mxw)==cnt:
  print(mxh+mxw-1)
else:
  print(mxh+mxw)
