import numpy as np

N, K=map(int, input().split())
A=np.sort(list(map(int, input().split())))

p=np.sum(A>0)
q=np.sum(A<0)
Z=N-p-q
if p>0:
  AP=A[-p:]
else:
  AP=[]
if q>0:
  AN=A[:q]
else:
  AN=[]

b=(N-Z)*Z+Z*(Z-1)//2
a=p*q

if K<=a:
  x=AP[-1]*AN[0]-1
  y=AP[0]*AN[-1]
  while y-x>1:
    tmp=(y+x)//2
    counter=np.searchsorted(AN, tmp//AP, side='right').sum()
    if counter<K:
      x=tmp
    else:
      y=tmp
  print(y)
elif K<=a+b:
  print(0)
else:
  x=0
  y=10**18
  K=K-a-b
  if q<=1:
    while y-x>1:
      tmp=(y+x)//2
      counter=(np.searchsorted(AP, tmp//AP, side='right').sum()-np.searchsorted(AP, int(pow(tmp, 1/2)), side='right'))//2
      if counter<K:
        x=tmp
      else:
        y=tmp
    print(y)
    return
    
  AN=AN[::-1]
  AN=-AN
  
  if p<=1:
    while y-x>1:
      tmp=(y+x)//2
      counter=(np.searchsorted(AN, tmp//AN, side='right').sum()-np.searchsorted(AN, int(pow(tmp, 1/2)), side='right'))//2
      if counter<K:
        x=tmp
      else:
        y=tmp
    print(y)
    return
    
  while y-x>1:
    tmp=(y+x)//2
    counter1=(np.searchsorted(AP, tmp//AP, side='right').sum()-np.searchsorted(AP, int(pow(tmp, 1/2)), side='right'))//2
    counter2=(np.searchsorted(AN, tmp//AN, side='right').sum()-np.searchsorted(AN, int(pow(tmp, 1/2)), side='right'))//2
    counter=counter1+counter2
    if counter<K:
      x=tmp
    else:
      y=tmp
  print(y)
