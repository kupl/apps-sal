from sys import stdin
mod = 998244353
def solveAsPolynomial():
    import numpy as np
    N,S = list(map(int,stdin.readline().split()))
    a = list(map(int,stdin.readline().split()))
    ans = 0
    f = np.zeros(S+1,np.int64)#f[k] := ある多項式のx**kの係数
    for A in a:
        #f = (f+1)(1+x**A)として更新していく
        f[0] += 1#f+1
        f[A:] += f[:-A].copy()#f*(1+x**A)
        f %= mod
        ans += f[S]
        #x**S = X**(A_1+...+A_k)ゆえ、f[S]は知りたい組み合わせの数と等しい
        ans %= mod
    return ans
def main():
  ans = solveAsPolynomial()
  print(ans)
def __starting_point():
  main()

__starting_point()
