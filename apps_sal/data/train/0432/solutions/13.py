class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0: return False

        C = Counter(nums)


        while C:
            start = min(C)
            for i in range(start, start + k):
                if i not in C: return False
                if C[i] == 1: del C[i]
                else: C[i] -= 1
        return True
