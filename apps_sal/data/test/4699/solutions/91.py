n,k=map(int,input().split());a=set(input().split())
while True:
  if not set(str(n))&a: print(n);break
  n+=1
