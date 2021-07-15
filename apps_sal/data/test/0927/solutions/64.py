def main():  
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  dp=[2,5,5,4,5,6,3,7,6]
  p=[]
  q=[]
  for i in range(M):
    p.append(dp[A[i]-1])
    q.append(A[i])
  bp=[[0,0]for i in range(N+1)]
  for i in range(N-1):
    for j in range(len(p)):
      if i+p[j]>N:
        continue
      if bp[i][0]==0:
          if i!=0:
              continue
      bp[i+p[j]][0]=max(bp[i+p[j]][0],bp[i][0]+(10**bp[i][1])*q[j])
      bp[i+p[j]][1]=bp[i][1]+1
  print(bp[N][0])
def __starting_point():
  main()
__starting_point()
