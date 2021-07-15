X,N=list(map(int,input().split()))

if N==0:
    print(X)
    return
poe=list(map(int,input().split()))
for i in range(101):
    if X-i not in poe:
        print((X-i))
        return
    elif X+i not in poe:
        print((X+i))
        return

