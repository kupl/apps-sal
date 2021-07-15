x,y = list(map(int,input().split()))

for a in range(x+1):
    for b in range(x-a+1):
        if a+b == x and 2*a+4*b == y:
            print('Yes')
            return
print('No')

