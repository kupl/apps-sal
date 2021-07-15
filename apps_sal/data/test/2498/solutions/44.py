from functools import reduce

def main():
  N,M=map(int,input().split())
  *A,=map(int,input().split())

  A = list(set(A))
  N = len(A)

  B = [A[i]//2 for i in range(N)]

  def factorize(n):
      out=[]
      i = 2
      while i==2:
          if n%i==0:
              out.append(i)
              n //= i
          else:
              i += 1
          if n == 1:break
          if i > int(n**.5+3):
              out.append(n)
              break
      return out

  ord_list=[len(factorize(B[i])) for i in range(N)]

  if len(set(ord_list)) != 1:
    print(0)
    return

  def gcd(a,b):
    if b == 0: return a
    return gcd(b,a%b)

  def lcm(a,b):
    return a*b//gcd(a,b)

  LCM = reduce(lcm,B)
  print((M//LCM+1)//2)
  
def __starting_point():
  main()
__starting_point()
