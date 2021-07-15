from collections import*
H,W=map(int,input().split());M=[input()for _ in"_"*H];C=[[1]*W for _ in"_"*H];q=deque([[0,0]])
while q:
  x,y=q.popleft()
  for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
    h,w=x+i,y+j
    if H>h>-1and W>w>-1and M[h][w]>'#'and C[h][w]<2:C[h][w]=C[x][y]+1;q.append([h,w])
c=C[H-1][W-1];print(-1*(c<2)or sum(m.count(".") for m in M)-c)
