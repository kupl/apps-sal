N,K=list(map(int,input().split()))
let=input()
can=0
for i in range(N-1):
   if let[i]!=let[i+1]:
      can+=1
if can<=K*2:
   print(N-1)
else:
   can-=K*2
   print(N-can-1)
