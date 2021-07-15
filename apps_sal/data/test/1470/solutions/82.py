import math
import numpy as np
import sys
input = sys.stdin.readline

def main():
    x = int(input())
    ans = 2*(x//11)
    x = x%11
    if x==0: pass
    elif x<7: ans += 1
    else: ans += 2
    print(ans)

main()
