for _ in range(int(input())):
  n,l=map(int,input().split())
  a=[0]+list(map(int,input().split()))+[l]
  b=[a[i+1]-a[i] for i in range(n+1)]
  ansl=0
  le=0
  lf=1
  ansr=0
  ri=n
  rf=1
  while le!=ri:
    if ansl+b[le]/lf<ansr+b[ri]/rf:
      ansl+=b[le]/lf
      le+=1
      lf+=1
    else:
      ansr+=b[ri]/rf
      ri-=1
      rf+=1
  t=b[le]
  ans=max(ansl,ansr)
  if ansl<ansr:
    t-=(ansr-ansl)*lf
  if ansl>ansr:
    t-=(ansl-ansr)*rf
  print(ans+t/(lf+rf))
