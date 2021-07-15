N=int(input())
mod=10**9+7
memo=[{} for _ in range(N+1)]

def ok(x, y, z, nx):
  if y=='A' and z=='G' and nx=='C':
    return False
  if x=='A' and z=='G' and nx=='C':
    return False
  if y=='G' and z=='A' and nx=='C':
    return False
  if y=='A' and z=='C' and nx=='G':
    return False
  if x=='A' and y=='G' and nx=='C':
    return False
  return True

def f(num,A):
  if num==N:
    return 1
  else:
    x,y,z=A[0],A[1],A[2]
    if (x,y,z) in memo[num]:
      return  memo[num][(x,y,z)]
    else:
      s=0
      for i in ['A','C','G','T']:
        if ok(x,y,z,i):
          s+=f(num+1,(y,z,i))
      memo[num][(x,y,z)]=s%mod
      return s%mod
print(f(0,'ZZZ'))
