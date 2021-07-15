#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    a,b,c,x,y = map(int,input().split())
    ans1=99999999999999999999999999
    if a+b>2*c:
        if x > y:
            ans1=2*c*y+a*(x-y)
        elif y > x:
            ans1=2*c*x+b*(y-x)
    ans2=c*2*max(x,y)
    ans3=a*x+b*y
    print(min(ans1,ans2,ans3))

def __starting_point():
    main()
__starting_point()
