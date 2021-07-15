import sys
from decimal import *

def main():
    n = int(sys.stdin.readline())

    x = list(map(int, sys.stdin.readline().split()))
    
    ans = []
    cur = 0
    for i in x:
        cur += i-1
        if cur%2==0:
            ans.append("2")
        else:
            ans.append("1")
    
    print("\n".join(ans))
    

main()

