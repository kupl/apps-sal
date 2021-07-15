n=int(input())
while True:
  if len(set(str(n)))==1:
    print(n)
    break
  n+=1
