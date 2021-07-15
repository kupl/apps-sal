N=int(input())
A=list(map(int,input().split()))
result=0
minimum=0
for a in A:
  if a>minimum:
    minimum=a
  elif a<minimum:
    result+=minimum-a
print(result)
