import sys
#import numpy as np
#from collections import defaultdict
import math
#from collections import deque

input = sys.stdin.readline
#import numpy as n



def main():

    N = int(input())
    ans =0
    for i in range(1,N+1):
        num =   N//i
        ans += num*(num+1)//2 *i

    print(ans)





def __starting_point():
    main()

__starting_point()
