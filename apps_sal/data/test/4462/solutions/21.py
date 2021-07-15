n=int(input())
a=list(map(int, input().split()))
x = 0
y = 0
for i in a:
    if i %2 != 0:
        x+=1
    elif i%4 == 0:
        y+=1
if y >=x:
    print('Yes')
    return
else:
    if x+y == len(a) and y == x-1:
        print('Yes')
    else:
        print('No')
