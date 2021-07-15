def yakusu(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
N,K=map(int,input().split())
L=list(map(int,input().split()))
a=sum(L)
R=yakusu(a)[::-1]
for i in range(len(R)):
  add=0
  minus=0
  s=R[i]
  A=list()
  B=list()
  for j in range(N):
    k=L[j]
    a=k%s
    b=s-a
    if a>b:
      add+=b
      B.append(b)
    elif a<b:
      minus+=a
      A.append(a)
    else:
      add+=a
      B.append(a)
  #足した分=add else:minus どっちでも:even
  A=sorted(A)
  B=sorted(B)
  if minus==add:
    d=minus
    if d<=K:
      print(s)
      return
  elif minus>add:
    q=(minus-add)//s
    d=sum(A[:len(A)-q])
    if d<=K:
      print(s)
      return
  else:
    q=(add-minus)//s
    d=sum(B[:len(B)-q])
    if d<=K:
      print(s)
      return
