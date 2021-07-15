class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        h = Counter(nums)
        unique = sorted(h.keys())
        for i in unique:
            while h[i] > 0:
                h[i] -= 1
                for j in range(i+1, i+k):
                    if h[j] <= 0:
                        return False
                    h[j] -= 1
        return True
