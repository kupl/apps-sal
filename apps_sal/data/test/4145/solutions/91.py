n=int(input())
while any(n%i==0 for i in range(2,n)):
  n+=1
print(n)
