N=int(input())
T=[0]*(N+1);S=[0]*(N+1);f=0
for i in range(1,N+1):
  t,x,y=map(int,input().split())
  T[i]=t
  S[i]=[x,y]
T[0]=0;S[0]=[0,0]

#print(T)
#print(S)

for i in range(1,N+1):
  if (T[i]-T[i-1])<(abs(S[i][0]-S[i-1][0])+abs(S[i][1]-S[i-1][1])):
    f=1
  if (T[i]-T[i-1])%2!=(abs(S[i][0]-S[i-1][0])+abs(S[i][1]-S[i-1][1]))%2:
    f=1

print("Yes" if f==0 else "No")
