import sys, random, math
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def main():
    inf = 10 ** 20

    t = int(input())
#    t, a, b = map(int, input().split())
#    t = 1
    
    for _ in range(1, t+1):
    #    print("Case #{}: ".format(_), end = '')
        
        n, m, k = map(int, input().split())
        each = n // k
        best = min(each, m)
        m -= min(each, m)
        sec = m // (k-1)
        if(m % (k-1)):
            sec += 1
        print(best - sec)
        
        
main()
