n,k=list(map(int, input().split()))
i=0
while True:
  if k**i>n:
    print(i)
    break
  i+=1

