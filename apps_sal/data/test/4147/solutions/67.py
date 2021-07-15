N,A,B,C= list(map(int,input().split()))
l=[]
Inf=float("Inf")
for i in range(N):l.append(int(input()))
def Answer(cnt,a,b,c):
   if cnt==N:
      return abs(A-a)+abs(B-b)+abs(C-c)-30 if min(a,b,c)>0 else Inf
   pt1=Answer(cnt+1,a,b,c)
   pt2=Answer(cnt+1,a+l[cnt],b,c)+10
   pt3=Answer(cnt+1,a,b+l[cnt],c)+10
   pt4=Answer(cnt+1,a,b,c+l[cnt])+10
   return(min(pt1,pt2,pt3,pt4))
print(Answer(0,0,0,0))
