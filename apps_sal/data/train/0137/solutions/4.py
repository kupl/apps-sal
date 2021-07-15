from functools import lru_cache

# removehigh = [(1 << l) - 1 for l in range(31)]
@lru_cache()
def removehigh(l: int) -> int:
    if l <= 1:
        return l + 1
    return (1 << l)
    
@lru_cache()
def sethigh(l: int, n: int) -> int:
    if n == 0:
        return removehigh(l) - 1
    
    t2 = 1 << l - 2
    
    if n >= t2:
        return removehigh(l - 1) + remove(n - t2)
    
    if n & (n - 1) == 0:
        return removehigh(l) - removehigh(n.bit_length())
    
    return removehigh(l - 1) + sethigh(l - 1, n) 

    
@lru_cache()
def remove(n: int) -> int:
    if n <= 1:
        return n
    elif n <= 3:
        return 5 - n
    
    l = n.bit_length()
    if n & (n - 1) == 0:
        return removehigh(l) - 1
    
    t3 = 3 << l - 2
    if n >= t3:
        return removehigh(l - 1) + remove(n - t3)
    
    t1 = 1 << l - 1
    return removehigh(l - 1) + sethigh(l - 1, n - t1) 



class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        return remove(n)

