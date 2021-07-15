import math, sys
from fractions import *

def mp():
    return list(map(int, input().split()))

def main():
    t = int(input())
    for i in range(t):
        l, r = mp()
        print(l, l * 2)
deb = 0
if deb:
    file = open('input.txt', 'w')
else:
    input = sys.stdin.readline
    
main()
