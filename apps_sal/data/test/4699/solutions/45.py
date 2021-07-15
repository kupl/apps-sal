n,k=map(int,input().split())
d=list(map(str,input().split()))
e=set(d)
for i in range(n,100001):
  v = set(str(i))&e
  if len(v)== 0:
    print(i);return
