def func(x, c2, c5):
    if x < 0:
        return -x * c5
    else:
        return x * c2
def func_2(x, c4, c1):
    if x < 0:
        return -x*c4
    else:
        return x*c1

def func_3(x, c6, c3):
    if x < 0:
        return -x*c3
    else:
        return x * c6

def main():
    y, x = map(int, input().split())
    c1, c2, c3, c4, c5, c6 = map(int, input().split())
    lu = (1,0)
    ru = (1,1)
    rd = (-1,0)
    r = (0, 1)
    l = (1, 0)
    ld = (-1, -1)
    a= func_3(y, c6, c3) + func(x, c2, c5)
    b =func_2(y, c4, c1) + func(x - y, c2, c5)
    c = func_2(x, c4, c1) + func_3(y - x, c6, c3)
    print(min(a,b,c))



def __starting_point():
    t = int(input())
    for i in range(t):
        main()
"""
123
1232
123232
23232123232
d(abc)e
ad(abc)e
Ad(abc)eC
dabe
adbeb
ebdadbeb
bebdadbeb
acccc
accccc
caccccc
ccccacaccccc
cccccacaccccc
"""
__starting_point()
