N=int(input())
s=0
for i in range(1,N+1):
  s+=i*(N//i)*(N//i+1)//2
print(s)
