import sys
lines = sys.stdin.read().splitlines()
lincnt = -1 

def input():
    nonlocal lincnt
    lincnt += 1
    return lines[lincnt]


for _ in range(int(input())):
    n = int(input())
    s = input()
    print(n * s[n-1])


