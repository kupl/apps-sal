n,m,x = map(int,input().split())
a = list(map(int,input().split()))
i = 0
j = 0
for k in a:
    if k>x:
        i += 1
    elif k<x:
        j += 1
print(min(i,j))
