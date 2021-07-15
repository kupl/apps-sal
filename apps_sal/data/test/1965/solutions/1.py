for _ in range(int(input())):
  n,x=map(int,input().split())
  a=list(map(int,input().split()))
  if a==[x]*n:
    print(0)
  elif sum(i-x for i in a)==0 or x in a:
    print(1)
  else:
    print(2)
