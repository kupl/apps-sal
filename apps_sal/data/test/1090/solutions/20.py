N,K=map(int,input().split())

S=input()
face2face=0
back2back=0
for i in range(N-1):
  if S[i]=='L' and S[i+1]=='R':
    back2back+=1
  if S[i]=='R' and S[i+1]=='L':
    face2face+=1


for i in range(K):
  face2face-=1
  back2back-=1
face2face=max(face2face,0)
back2back=max(back2back,0)
  
print(N-face2face-back2back-1)
