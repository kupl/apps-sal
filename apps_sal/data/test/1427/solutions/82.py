import math
MOD = 10**9+7

N = int(input())
A = list(map(int,input().split()))
A.sort()
MAX = max(A[-1],2)

C = [0 for _ in range(MAX+1)]

for a in A:
  C[a] += 1

ans = 1
P = [1 for _ in range(MAX+1)] #素数かどうか
P[0] = 0
P[1] = 0
S = [0 for _ in range(MAX+1)] #最小公倍数の素因数分解したもの
for i in range(MAX+1):
  #素数でないなら以下の手順を行わない
  if P[i] == 0:
    continue
  #エラトステネスの篩
  k = i*2
  while k <= MAX:
    P[k] = 0
    k += i
  ind = 0
  k = 1
  while k <= MAX:
    k *= i
    ind += 1
  k = k // i 
  ind -= 1
  #最大のべきを調べる
  while k > 1:
    l = k
    flag = False
    while l <= MAX:
      if C[l] > 0:
        flag = True
        break
      l += k
    if flag:
      break
    k = k // i
    ind -= 1
  S[i] = ind
  ans *= pow(i,ind,MOD)
  ans %= MOD
  
#モジュラ逆数
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    #if g != 1:
        #raise Exception('modular inverse does not exist')
    #else:
    return x % m
      
B = [0 for _ in range(MAX+1)]
ans_2 = 0
for a in A:
  if B[a] > 0:
    ans_2 += B[a]
  else:
    B[a] = modinv(a, MOD)
    ans_2 += B[a]    
  ans_2 %= MOD 

#print(ans, ans_2, P, S, B)
print(((ans * ans_2) % MOD))
  


