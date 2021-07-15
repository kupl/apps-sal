from math import gcd
MOD = 1000_000_007

N = int(input())

Fish = {}
zeros = 0

for i in range(N):
  A, B = list(map(int,input().split())) 
  if A == 0 and B == 0:
    zeros += 1
    continue
  
  G = gcd(abs(A), abs(B))
  A, B = A // G, B // G
  if A < 0:
    A *= -1
    B *= -1
  elif A == 0:
    B = 1
    
  if (A, B) not in Fish:
    Fish[(A, B)] = 1
  else:
    Fish[(A, B)] += 1

#print(Fish)
done_set = set()

ans = 1
for (a, b) in list(Fish.keys()):
  #print(a,b)
  if b > 0:
    c = b
    d = -a
  elif b == 0:
    c = 0
    d = 1
  else: 
    c, d = -b, a
  
  #print(done_set)
  #print((a,b), (c,d), done_set)
  if (a, b) in done_set or (c, d) in done_set: 
    continue
  #print((a,b), Fish[(a,b)])
  #print((c,d), Fish[(c,d)])
  if (c, d) not in list(Fish.keys()):
    
    ans *= pow(2, Fish[(a,b)], MOD)
  else:
    ans *= (1 + (pow(2, Fish[(a,b)], MOD)-1) + (pow(2, Fish[(c,d)], MOD)-1))  
    done_set.add((c,d))
  ans %= MOD
  
  #print(done_set, ans)
  done_set.add((a,b))
  
ans += zeros
ans -= 1
ans %= MOD
#print(zeros)
print(ans)

  

