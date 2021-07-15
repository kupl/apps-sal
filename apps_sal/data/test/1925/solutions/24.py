a,b,n = map(int,input().split())

num = min(b-1,n)

print(int((a*num)/b)-a*int(num/b))
