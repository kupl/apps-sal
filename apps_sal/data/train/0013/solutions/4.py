import sys
input = sys.stdin.readline

t=int(input())
for tests in range(t):
    n,g,b=list(map(int,input().split()))
    ALL=(n+1)//2

    ANS=n

    week=-(-ALL//g)-1
    ANS=max(ANS,week*(g+b)+(ALL-week*g))

    print(ANS)

