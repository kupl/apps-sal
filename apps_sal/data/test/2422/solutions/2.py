import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    if n == 1 or n == 2 or n == 4:
        print(-1)
    else:
        if n% 3 == 2:
            print(n//3-1,1,0)
        elif n % 3==1:
            print(n//3-2,0,1)
        else:
            print(n//3,0,0)     
