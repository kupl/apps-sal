import sys
pin=sys.stdin.readline
def main():
  N,M=map(int,pin().split())
  d=[list(map(int,pin().split())) for _ in [0]*N]
  d.sort()
  cnt=0
  ans=0
  for i in d:
    if M<=cnt+i[1]:
      ans+=i[0]*(M-cnt)
      print(ans)
      return
    cnt+=i[1]
    ans+=i[0]*i[1]
  print(ans)
  return
main()
