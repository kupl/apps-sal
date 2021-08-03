class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = Counter(nums)
        while c:
            x = min(c.keys())
            for i in range(x, x + k):
                if i not in c:
                    return False
                c[i] -= 1
                if c[i] == 0:
                    del c[i]
        return True
