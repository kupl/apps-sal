a,b=map(int,input().split())
if a%2==0 and b%2==0:
  if (b-a)%4==0:
    print(b)
  else:
    print(b^1)
elif a%2==0:
  if (b-a)%4==1:
    print(1)
  else:
    print(0)
elif b%2==0:
  if (b-a)%4==1:
    print(a^b)
  else:
    print(a^b^1)
else:
  if (b-a)%4==0:
    print(a)
  else:
    print(a^1)
