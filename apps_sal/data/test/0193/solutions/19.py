import math,string,itertools,fractions,heapq,collections,re,array,bisect
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict, deque

def VI(): return list(map(int,input().split()))





def main(info=0):
    a,b = VI()
    c,d = VI()

    # the problem intend was to use some optimization / binary search, but a
    # deterministic solution has been proposed and is used here.  idea: given
    # A, the matrix B is same as A, with +/-x at every element (plus/minus
    # depend on the signs of A elements. It's easiest to compute all possible
    # cases (only 4). Then, we can formulate the equation for the determinant
    # of this B, and set it to 0.
    # This leads to:
    #
    # det(B) == 0 == ad-bc-x(a+b+c+d)+x^2-x^2 == ad-bc-x(a+b+c+d)+x^2-x^2
    #
    # since the first two terms are the determinant of A, and the last two go
    # away, we get:
    #
    # 0 == det(A) - x(a+b+c+d)  <==>   x=det(A)/(a+b+c+d)
    #
    # after taking care of the other signs, one gets other potential solutions
    # below.
    #
    # However, as has been noted, it has not been proven that this is the
    # optimal solution. But it seems to be.

    detA = a*d-b*c

    denom = max(abs(a + b + c + d), abs(a + d - c - b),
                abs(a + c - b - d), abs(a + b - c - d))
    ans = 0 if detA == 0 else abs(detA/denom)
    print(ans)



def __starting_point():
    main()

__starting_point()
