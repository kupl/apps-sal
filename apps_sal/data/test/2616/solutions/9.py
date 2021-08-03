#import sys
# sys.setrecursionlimit(10**9)
for tt in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    won = 0
    for i in range(n - 1):
        if(a[i] == 1):
            won = (won + 1) % 2
        elif(a[i + 1] == 1):
            a[i + 1] = 2
    if(won == 0):
        print("First")
    else:
        print("Second")
