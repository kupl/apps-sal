import sys
import math

def main():
    n, k, M, D = map(int, input().split())
    
    ans = 1
    for i in range(1, D + 1):
        d = (k * (i - 1) + 1)
        
        left = (n // (i * k))
        right = n // d
        
        cnt = 1
        if (M <= right):
            cnt = M
        else:
            cnt = right
            
        added = cnt * i
        ans = max(ans, added)
        
    print(ans)
            
    
def __starting_point():
    main()
__starting_point()
