a,b=map(int,input().split())
 
def prime_factorization(n):
  if n==1:
    return [1]
  else:
    i=2
    ans=[]
    k=int(n**0.5)+1
    for j in range(2,k+1):
      if n==1: break
      if n%j==0:
        n//=j
        ans.append(j)
        while n%j==0:
          n//=j
    if len(ans):
      ans.append(1)
      if n!=1:
        ans.append(n)
      return ans
    else:
      return [1,n]

A=prime_factorization(a)
B=prime_factorization(b)
 
print(len(set(A)&set(B)))
