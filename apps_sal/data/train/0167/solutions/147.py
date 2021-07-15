from functools import lru_cache
from typing import Tuple

class Solution:
    # floor: 0 <= F <= N
    # Ans f where eggs break if it's higher than f
    # N floors from 1 to N.
    # K eggs
    # Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 
    def superEggDrop(self, K: int, N: int) -> int:
        return superEggHelper(K, N)
        
            
        
        
        
@lru_cache(maxsize=None)
def superEggHelper(K: int, N: int) -> int:
    # base case
    if N == 0:
        return 0
    
    if K == 1:
        return N

    # ans = N;
    # dropping from floor i
    # for i in range(1, N + 1):
    #     ans = min(max(superEggHelper(K, N - i), superEggHelper(K - 1, i - 1)) + 1, ans)

    # bin search
    ans = bisectEggHelper(K, 1, N, N)

    # print(K, N, ans)
    return ans

# 2 0 1 1
# S: start, E: end, N: number of floors, K: number of eggs
def bisectEggHelper(K: int, S: int, E: int, N: int) -> int:
    # print(K, S, E, N)
    # base case, only one element left
    if S == E:
        left, right = superEggCalc(K, S, N)
        return max(left, right) + 1
    
    # base case, only two elements left
    if S + 1 == E:
        # K = 2
        # i = 0
        # S = 0
        # N = 1
        left1, right1 = superEggCalc(K, S, N)
        left2, right2 = superEggCalc(K, E, N)
        return min(max(left1, right1), max(left2, right2)) + 1

    # choose i = (S + E) // 2
    i = (S + E) // 2
    left, right = superEggCalc(K, i, N)
    if left > right:
        return bisectEggHelper(K, S, i, N)
    else:
        return bisectEggHelper(K, i, E, N)
   
def superEggCalc(K: int, i: int, N: int) -> Tuple:
    return (superEggHelper(K - 1, i - 1), superEggHelper(K, N - i))

