a,b,x,y = list(map(int,input().split()))
num = a - b
if num == 0:
    print(x)
elif num < 0:
    num = abs(num)
    ans = x
    if num * y > num * (x * 2):
        print((ans + (num * (x * 2))))
    else:
        print((ans + (num * y)))
else:
    num -= 1
    ans = x
    if num == 0:
        print(ans)
    else:
        if num * y > num * (x*2):
            print((ans + (num * (x*2))))
        else:
            print((ans + (num * y)))

