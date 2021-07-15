S = input()
N = len(S)
a,b,c,d = 0,0,0,1
mod = 10**9+7
for x in reversed(S):
  if x == "?":
    a,b,c,d = 3*a+b, 3*b+c, 3*c+d, 3*d
  elif x == "A":
    a += b
  elif x == "B":
    b += c
  elif x == "C":
    c += d
  a %= mod; b %= mod; c %= mod; d %= mod
print(a)
