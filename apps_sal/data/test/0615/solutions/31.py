import sys, os
from itertools import accumulate
import bisect

f = lambda:list(map(int,input().split()))
if 'local' in os.environ :
    sys.stdin = open('./input.txt', 'r')

n = f()[0]
def get_mid(b, i):
    nonlocal n
    front_i_sum = b[i]

    idx1 = bisect.bisect_right(b, front_i_sum/2)
    if idx1 == 0:
        idx1 = 1
        max_fisrt = max(b[0], b[i]-b[0])
        min_first = min(b[0], b[i]-b[0])
    
    else:


        max1 = b[idx1]
        min1 = b[i] - b[idx1]

        max2 = b[i] - b[idx1-1]
        min2 = b[idx1-1]

        if max1 - min1 >= max2 - min2:
            max_fisrt = max2
            min_first = min2
        else:
            max_fisrt = max1
            min_first = min1


    idx2 = bisect.bisect_right(b, front_i_sum + (b[n-1] - b[i])/2)

    if idx2 == i+1:
        max_s = max(b[i+1]- b[i], b[n-1]- b[i+1])
        min_s = min(b[i+1]- b[i], b[n-1]- b[i+1])

    else:
        max1 = b[idx2] - front_i_sum
        min1 = b[n-1] - b[idx2]

        max2 = b[n-1] - b[idx2-1]
        min2 = b[idx2-1] - front_i_sum

        if max1 - min1 >= max2 - min2:
            max_s = max2
            min_s = min2
        else:
            max_s = max1
            min_s = min1
    
    return max(max_fisrt, max_s) - min(min_first, min_s)


def solve():
    a = f()
    b = list(accumulate(a))

    ans = int(2e14)
    for i in range(1, n-2):
        ans = min(ans, get_mid(b, i))

    print(ans)




solve()

