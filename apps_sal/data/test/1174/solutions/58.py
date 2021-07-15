'''
Created on 2020/09/09

@author: harurun
'''
def main():
  import heapq
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N,M=map(int,pin().split())
  A=list(map(int,pin().split()))
  B=list(map(lambda x: -x ,A))
  heapq.heapify(B)
  for i in range(M):
    t=heapq.heappop(B)
    s=-((-t)//2)
    heapq.heappush(B,s)
  ans=0
  for j in range(N):
    q=heapq.heappop(B)
    ans+=(-q)
  print(ans)
  return
main()
