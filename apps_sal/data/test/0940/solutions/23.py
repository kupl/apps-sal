a,b,c = [int(s) for s in input().split()]
su = a+b+c
ma = max(a,b,c)
print(max(0, 2*ma-su+1))
