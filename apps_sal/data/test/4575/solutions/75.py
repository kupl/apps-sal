N=int(input())
kazu=input().split(' ')
D=int(kazu[0])
X=int(kazu[1])
days=[]
count=0
for i in range(N):
  days.append(int(input()))
for i in range(N):
  a=0
  while 1:
    b=days[i]*a+1
    if b>D:
      break
    count=count+1
    a=a+1
print(count+X)
