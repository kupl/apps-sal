import math
t = int(input())
for turn in range(t):
    x,n,m = map(int,input().split())
    while x >= 19 and n > 0:
        x = (x//2) + 10
        n -= 1
    if x > 10 * m:
        print("NO")
    else:
        print("YES")
