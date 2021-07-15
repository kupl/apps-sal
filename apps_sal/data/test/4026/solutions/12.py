
from sys import stdin

tt = int(stdin.readline())

for loop in range(tt):

    n,m = map(int,stdin.readline().split())
    ans = "NO"

    for i in range(n):

        a,b = map(int,stdin.readline().split())
        c,d = map(int,stdin.readline().split())

        
        if b == c and m % 2 == 0:
            ans = "YES"

    print (ans)
