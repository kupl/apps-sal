t = int(input())

for _ in range(t):
    r,g,b,w = list(map(int,input().split()))
    if r%2 + g%2 + b%2 + w%2 <= 1:
        print('Yes')
        continue
    if r>0 and g>0 and b>0:
        r -= 1
        g -= 1
        b -= 1
        w += 3
        if r%2 + g%2 + b%2 + w%2 <= 1:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

