class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        c = collections.Counter([i % k for i in arr])
        for j in c:
            if j == 0:
                if c[j] % 2 != 0:
                    return False
            elif c[j] != c[k - j]:
                return False
        return True
