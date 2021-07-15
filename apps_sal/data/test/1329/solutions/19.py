def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

n=int(input())
alist=[0]*101
for i in range(2,n+1):
  for j in factorization(i):
    alist[j[0]]+=j[1]
if n==1:
  print(0)
else:
  ans=0
  for i in range(1,100):
    if alist[i]>=74:
      ans+=1
    if alist[i]>=24:
      for j in range(1,100):
        if i!=j and alist[j]>=2:
          ans+=1
    if alist[i]>=14:
      for j in range(1,100):
        if i!=j and alist[j]>=4:
          ans+=1
    if alist[i]>=2:
      for j in range(1,100):
        for k in range(j+1,100):
          if i!=j and  k!=i and alist[j]>=4 and alist[k]>=4:
            ans+=1
  print(ans)
