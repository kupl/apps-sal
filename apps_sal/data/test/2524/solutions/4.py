def main():
  n=int(input())
  a=list(map(int,input().split()))
  div,ans=1,0
  mod=10**9+7
  for i in range(60):
    cnt=0
    for j in a:
      cnt+=(j>>i)&1
    ans+=(cnt*(n-cnt)*div)%mod
    div=(div*2)%mod
  print(ans%mod)
  
def __starting_point():
  main()
__starting_point()
