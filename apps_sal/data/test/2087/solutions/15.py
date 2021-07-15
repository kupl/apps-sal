mod = 998244353
def main():
  a, b, c = map(int, input().split())
  a = a*(a+1)//2%mod
  b = b*(b+1)//2%mod
  c = c*(c+1)//2%mod
  print(a*b%mod*c%mod)
  
def __starting_point():
  main()
__starting_point()
