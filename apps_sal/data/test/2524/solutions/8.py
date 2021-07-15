def main():
  N=int(input())
  A=list(map(int,input().split()))
  mod=10**9+7
  ans=0
  for i in range(60):
    c=0
    for j in A:
      if j>>i&1:
        c+=1
    ans+=pow(2,i,mod)*c*(N-c)
    ans%=mod
  print(ans)
def __starting_point():
  main()
__starting_point()
