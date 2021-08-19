class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if k == 1:
            return True
        c = collections.Counter(nums)
        for num in nums:
            start = num
            while c[start - 1]:
                start -= 1
            while start <= num:
                while c[start]:
                    for j in range(k):
                        if not c[start + j]:
                            return False
                        c[start + j] -= 1
                start += 1
        return True
