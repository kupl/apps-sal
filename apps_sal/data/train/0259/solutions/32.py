class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 0
        r = nums[-1]
        res = []
        while r-l > 1:
            c = (l+r)//2
            tmp_sum = [math.ceil(i/c) for i in nums]
            tmp_sum = sum(tmp_sum)
            if tmp_sum > threshold:
                l = c
            elif tmp_sum <= threshold:
                r=c
                res.append(c)
        return min(res)
            

