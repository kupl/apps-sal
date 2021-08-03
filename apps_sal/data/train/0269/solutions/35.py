class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dis = k
        for n in nums:
            if n:
                if dis < k:
                    return False
                else:
                    dis = 0
            else:
                dis += 1
        return True
