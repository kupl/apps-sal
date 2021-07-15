w,a,c=map(int,input().split())

b=w+a
d=w+c

if a>c:
  if a>d:
    print(abs(d-a))
  else:
    print('0')

else:
  if c>b:
    print(abs(c-b))
  else:
    print('0')
