import sys
import math

def input():
    return sys.stdin.readline().strip()
def iinput():
    return int(input())
def tinput():
    return input().split()
def rinput():
    return list(map(int, tinput()))
def rlinput():
    return list(rinput())

def main():
    n = iinput()
    res = 10
    q = 1
    while res <= n:
        res *= 10
        q += 1
    res //= 10
    q -= 1
    for i in range(q):
        res += 10 ** i
    ans = 0
    i = 1
    while res <= n and i <= 9:
        ans += 1
        res = res //i * (i + 1)
        i += 1
        
    
    
    
    print(9 * q + ans)
    
for i in range(iinput()):
    main()

