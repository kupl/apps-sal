n=int(input())
x=list(map(int,input().split()))
st=sorted(x)
a=st[len(st)//2-1]
b=st[len(st)//2]

for i in x:
  if i<=a:
    print(b)
  else:
    print(a)

