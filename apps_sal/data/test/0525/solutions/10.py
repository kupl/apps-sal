import sys
input = sys.stdin.readline
t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    s = set(l)
    if(len(s) == 1):
        print(n)
    else:
        print(1)
    t -= 1
