# import sys
# input = sys.stdin.readline
n = int(input())

def gcd(x,y):
    while x != 0 and y != 0:
        x,y = max(x,y),min(x,y)
        x %= y
    return y
for i in range(n):
    a, b = map(int,input().split())
    if gcd(a,b) == 1:
        print("Finite")
    else:
        print("Infinite")
