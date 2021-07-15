import math, collections, sys
input = sys.stdin.readline
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) == 1:
        if a[0]%2:
            print(-1)
        else:
            print(1)
            print(1)
    else:
        flag = -1
        for i in range(n):
            if a[i]%2 == 0:
                flag = i+1
        if flag != -1:
            print(1)
            print(flag)
        else:
            print(2)
            print(1, 2)
for _ in range(int(input())):
    solve()
