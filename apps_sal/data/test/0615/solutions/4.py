import bisect

n=int(input())
arr=list(map(int,input().split()))
acum=[0]
for i in range(n):
  acum.append(acum[-1]+arr[i])
ans=10**18
for i in range(2,n-1):
  suma=acum[i]
  sumb=acum[n]-suma
  posa=bisect.bisect_right(acum,suma//2)
  diffa=10**18
  if posa>=2:
    mina=min(acum[posa-1],acum[i]-acum[posa-1])
    maxa=max(acum[posa-1],acum[i]-acum[posa-1])
    diffa=maxa-mina
  if posa!=i:
    tmina=min(acum[posa],acum[i]-acum[posa])
    tmaxa=max(acum[posa],acum[i]-acum[posa])
    tdiffa=tmaxa-tmina
    if tdiffa<diffa:
      diffa=tdiffa
      mina=tmina
      maxa=tmaxa
  posb=bisect.bisect_right(acum,suma+sumb//2)
  diffb=10**18
  if posb>=i+2:
    minb=min(acum[posb-1]-acum[i],acum[n]-acum[posb-1])
    maxb=max(acum[posb-1]-acum[i],acum[n]-acum[posb-1])
    diffb=maxb-minb
  if posa!=n+1:
    tminb=min(acum[posb]-acum[i],acum[n]-acum[posb])
    tmaxb=max(acum[posb]-acum[i],acum[n]-acum[posb])
    tdiffb=tmaxb-tminb
    if tdiffb<diffb:
      diffb=tdiffb
      minb=tminb
      maxb=tmaxb
  ans=min(ans,max(maxa,maxb)-min(mina,minb))
print(ans)
