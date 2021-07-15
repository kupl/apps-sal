from math import ceil as cc
def mi():
    return map(int, input().split())
'''
5
2 3
10 10
2 4
7 4
9 3
'''
n = int(input())
for i in range(n):
    a,b = mi()
    if a==b:
        print(0)
    elif (b-a)%2==0 and b>a:
        print(2)
    elif (b-a)%2 and b>a:
        print(1)
    elif (b-a)%2==0 and b<a:
        print(1)
    else:
        print(2)
