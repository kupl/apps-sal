a,b=map(int,input().split())

def xor(n):
  z=n%4
  if z==0:
      return n
  elif z==1:
      return 1
  elif z==2:
      return n+1
  else:
      return 0


xxx=xor(b)^xor(a-1)

print(xxx)
