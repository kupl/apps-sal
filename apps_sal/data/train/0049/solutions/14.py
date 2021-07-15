import math

def check(x):
    cnt = 0
    while(x):
        cnt = cnt + (x%10 != 0)
        x = math.floor(x/10)
    return cnt<=3

def bl(x):
    ans = 0
    for i in range(1,x+1):
        if check(i):
            ans = ans+1
    return ans


def jc(x):
    sm = 1
    for i in range(1,x+1):
        sm = sm * i
    return sm

def c(x,y):
    if x<y:
        return 0
    return jc(x)/(jc(x-y)*jc(y))

def cal1(x,y):
    ans = 0
    for i in range(1,min(x,y)+1):
        ans = ans + c(x,i)*(9**i)
    return ans+1

def revers(x):
    ans = 0
    while(x):
        ans = ans*10+ x%10
        x = x.__floordiv__(10)

    return ans

def cal2(x):
    rx = revers(x)
    ans = 0
    cnt = 0
    l = 0
    l_ = 0
    while(x):
        l = l+1
        x = x.__floordiv__(10)


    while(rx):
        now = rx % 10
        rx = rx.__floordiv__(10)
        l_ = l_ + 1
        if now!=0:
            cnt = cnt+1
        else:
            continue
        ans = ans + (now-1)*cal1(l-l_,3-cnt) + cal1(l-l_,3-cnt+1)

        if cnt>=3:
            break

    return ans

T = int(input())
for i in range(T):

    x,y = list(map(int,input().split()))

    print(int(cal2(y)-cal2(x-1)))

