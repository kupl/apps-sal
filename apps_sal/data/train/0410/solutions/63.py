@lru_cache(maxsize=1000)
def pow(n: int):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + pow(n//2)
    else:
        return 1 + pow(3 * n + 1)

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        l = list(range(lo, hi + 1))
        l.sort(key = lambda x: (pow(x),x) )
        return l[k-1]
