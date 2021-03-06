class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k > 0:
            return False
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for num in nums:
            if d[num] > 0 and (num - 1 not in d or d[num - 1] < d[num]):
                for _ in range(k):
                    if num not in d or d[num] == 0:
                        return False
                    d[num] -= 1
                    num += 1
        return True
