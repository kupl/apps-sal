a,b,c = map(int,input().split())
for i in range(a):
    if b * (i + 1) + c * (i + 2) > a:
        print(i)
        return
