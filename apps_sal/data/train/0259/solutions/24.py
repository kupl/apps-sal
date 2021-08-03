class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        val = sum(nums)
        n = len(nums)

        if val <= threshold:
            return 1

        p = val // threshold + int(val % threshold != 0)
        q = val // (max(1, threshold - n - 1))
        q = q + 4
        p = max(2, p)

        check = 1

        while (p < q):
            mid = (p + q) // 2
            count1 = 0
            count2 = 0
            for i in nums:
                count1 = count1 + (i // mid + int(i % mid != 0))
                count2 = count2 + (i // (mid - 1) + int(i % (mid - 1) != 0))
            if count1 <= threshold and count2 > threshold:
                return mid
            elif count1 <= threshold and count2 <= threshold:
                q = mid
            elif count1 > threshold:
                p = mid + 1
