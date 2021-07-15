n,k=map(int,input().split())
for i in range(10**5):
  if (i*(i+1))//2-(n-i)==k:
    print(n-i)
