H,W,D=map(int,input().split())
A=[list(map(int,input().split()))for _ in range(H)]
Q=int(input())
lr=[list(map(int,input().split()))for _ in range(Q)]

C={}
for i in range(H):
    for j in range(W):
        C[A[i][j]]=[j,i]

S=[0]*(H*W+1)
i=D+1
while i<H*W+1:
    x1,y1=C[i][0],C[i][1]
    x2,y2=C[i-D][0],C[i-D][1]
    S[i]=S[i-D]+abs(x2-x1)+abs(y2-y1)
    i+=1

for l,r in lr:
    q=S[r]-S[l]
    print(q)
