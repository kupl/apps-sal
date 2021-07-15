n,m = map(int,input().split())
a = list(map(int,input().split()))
x = 1
c = 0
for i in a:
    if c+i <= m:
        c+=i
    else:
        c = i
        x+=1
print(x)
