def main():
  H,W,D=list(map(int,input().split()))

  A=[[0,0] for i in range(H*W)]
  for h in range(H):
    for w,a in enumerate(map(int,input().split())):
      A[~-a][0],A[~-a][1]=h,w

  B=[0]*(H*W)
  for i in range(H*W-D):
    B[i+D]=B[i]+abs(A[i][0]-A[i+D][0])+abs(A[i][1]-A[i+D][1])

  for q in range(int(input())):
    l,r=list(map(int,input().split()))
    print((B[~-r]-B[~-l]))

main()

