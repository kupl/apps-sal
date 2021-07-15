X,N = map(int,input().split())
p = sorted([int(i) for i in input().split()])
a = X
b = X
for i in range(100):
    if(a not in p):
        print(a)
        return
    elif(b not in p):
        print(b)
        return
    else:
        a -= 1
        b += 1
