k=int(input())

if k%2==0:
  print(-1)
  return
  
if k%5==0:
  print(-1)
  return
  
if k%7==0:
  k=k//7

# m(r)=10**0+10**1+...+10**(r-1)
# 10*m(r)=10**1+10**2+...+10**r
# 9*m(r)=10**r-10**0
# m(r)=(10**r-1)/9

# m(r)%n=(10**r-1)/9%k=0
# (10**r-1)%(9*k)=0

# 10**r%(9*k)=1
# 10**r%(9*k)=(10**(r-1)%(9*k))*10%(9*k)=1

r=1
m=10
while True:
  m%=(9*k)
  #print(r,m)
  if m==1:
    print(r)
    return
  r+=1
  m*=10
