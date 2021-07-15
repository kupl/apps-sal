x,y = map(int,input().split())
cnt = 0
for b in range(x+1) :
    for t in range(x+1) :
        if x == b+t and y == 2*b+4*t :
            print('Yes')
            return
        else :
            continue
print('No')
