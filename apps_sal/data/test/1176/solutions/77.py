import sys
import math
import itertools
import collections
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    N = NI()
    A = NLI()
    
    cnt = 0
    minimum_abs = 10**9
    ans = 0
    flag = 0
    
    for n in range(N):
        ans += abs(A[n])
        minimum_abs = min(abs(A[n]),minimum_abs)
        if A[n] < 0:
            cnt += 1
        elif A[n] == 0:
          flag = 1

                
    if cnt % 2 == 0 or flag == 1:
        print(ans)
    else:
        print(ans - minimum_abs * 2)
            


def __starting_point():
    main()
__starting_point()
