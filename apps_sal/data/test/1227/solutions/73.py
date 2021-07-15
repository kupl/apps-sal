def calc(a,D,K):
  if K==1:
    return a+(D-1)*9
  elif K==2:
    return (a-1)*(D-1)*9 + (D-1)*(D-2)//2*81
  else:
    return (a-1)*(D-1)*(D-2)//2*81 + (D-1)*(D-2)*(D-3)//6*729

N=input()
K=int(input())
D = len(N)
score=0
for i,a in enumerate(N):
  if a!="0":
    score+=calc(int(a),D-i,K)
    K-=1
  if K==0:
    break
print(score)
