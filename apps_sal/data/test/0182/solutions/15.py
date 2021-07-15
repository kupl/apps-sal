a,b,c = list([int(x) for x in input().split(' ')])
x,y,z = list([int(x) for x in input().split(' ')])

if x-a>0 and y-b>0 and z-c>0:
    print('No')
elif x-a<=0 and y-b<=0 and z-c<=0:
    print('Yes')
else:
    n = 0
    if a-x < 0:
        n+=x-a
    if b-y < 0:
        n+=y-b
    if c-z < 0:
        n+=z-c

    t = 0
    if a-x >= 0:
        t+=(a-x)//2
    if b-y >= 0:
        t+=(b-y)//2
    if c-z >= 0:
        t+=(c-z)//2

    if t >= n:
        print('Yes')
    else:
        print('No')

