from functools import lru_cache

MOD = 10**9 + 7

@lru_cache(None)
def F(N):
  # (u,v) = (a^b,a+b), (a^b,a+b+1) という組の個数x,y. where v <= N
  if N == 0:
    return 1,1
  x,y = 0,0
  # (0,0) mod 2
  x1,y1 = F(N//2)
  x += x1
  y += x1
  # (0,1) mod 2
  x2,y2 = F((N-1)//2)
  x += x2
  y += y2
  # (1,1) mod 2
  if N > 1:
    x3,y3 = F((N-2)//2)
    x += y3
    y += y3

  return x%MOD,y%MOD
  
answer = F(int(input()))[0]
           
print(answer)
  
  

