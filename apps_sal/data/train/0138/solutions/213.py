class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return -1
        pos = 0
        neg = 0
        answer = 0
        for num in nums:
            if num == 0:
                answer = max(answer, pos)
                pos = neg = 0
                continue
            if num > 0:
                pos += 1
                neg += 1 if neg else 0
            else:
                orig_pos = pos
                pos = neg + 1 if neg else 0
                neg = (orig_pos + 1) if orig_pos else 1
            answer = max(answer, pos)
        return answer
