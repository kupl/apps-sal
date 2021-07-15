A,B,C = list(map(int,input().split()))
mod = 998244353


A = (((A+1)*A)//2) % mod
B = (((B+1)*B)//2) % mod
C = (((C+1)*C)//2) % mod
print(((A*B*C) % mod))

