n=int(input())
x=int(n**0.5)
for i in range(x):
  if n%(x-i)==0:
    y=n//(x-i)
    y=str(y)
    print(len(y))
    break
