import sys

def resolve():
    readline=sys.stdin.readline

    n=int(readline())
    a,b=map(int, readline().rstrip().split())
    for _ in range(n-1):
        x,y=map(int, readline().rstrip().split())
        start=max(a//x,b//y)
        for z in range(start,start+1000):
            if x*z>=a and y*z>=b:
                a,b=x*z,y*z
                break
    print(a+b)

    return

if 'doTest' not in globals():
    resolve()
    return
