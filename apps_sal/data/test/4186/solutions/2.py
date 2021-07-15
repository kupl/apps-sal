import math, sys
from fractions import *

def mp():
    return list(map(int, input().split()))

def main():
    n = int(input())
    a = sorted(mp())
    i = 0
    ans = 0 
    while i < n:
        ans += a[i + 1] - a[i]
        i += 2
    print(ans)
        
deb = 0
if deb:
    file = open('input.txt', 'w')
else:
    input = sys.stdin.readline
    
main()
