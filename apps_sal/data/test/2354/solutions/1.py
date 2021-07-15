import sys
input=sys.stdin.readline

n,q=map(int,input().split())
evenOneLine=(n+1)//2
evenTwoLine=n//2
oddOneLine=evenTwoLine
oddTwoLine=evenOneLine

for i in range(q):
    num=0
    x,y=map(int,input().split())
    if (x+y)%2==0:
        if x%2==1:
            num+=(x//2)*(evenOneLine+evenTwoLine)
            num+=(y//2)+1
            print(num)
        else:
            num+=(x-1)//2*(evenOneLine+evenTwoLine)+evenOneLine
            num+=(y-1)//2+1
            print(num)
    else:
        num=(n**2)//2
        if n%2==1: num+=1
        if x%2==1:
            num+=(x//2)*(oddOneLine+oddTwoLine)
            num+=(y-1)//2+1
            print(num)
        else:
            num+=(x-1)//2*(oddOneLine+oddTwoLine)+oddOneLine
            num+=y//2+1
            print(num)
