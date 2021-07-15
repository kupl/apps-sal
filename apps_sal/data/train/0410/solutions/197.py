from heapq import heapify, heappop

cache = {
    1: 0
}


def collatz(y):
    if y in cache:
        return cache[y]
    
    x = y
    steps = 1
    while x > 1:
        if x % 2 == 1:
            x = 3 * x + 1
        else:
            x //= 2
            
        if x in cache:
            ans = cache[x] + steps
            break

        steps += 1
    else:
        ans = steps

    cache[y] = ans
    return ans


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = [(collatz(x), x) for x in range(lo, hi + 1)]
        heapify(powers)
        
        for _ in range(k):
            x = heappop(powers)

        return x[1]
