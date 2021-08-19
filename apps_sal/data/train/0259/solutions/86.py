class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        r = max(nums)
        l = 1

        def calc(div):
            s = sum([(num + div - 1) // div for num in nums])
            return s <= threshold

        while l < r:
            mid = (l + r) // 2
            val = calc(mid)
            # print (\"[%d, %d] => %d v %r\" %(l, r, mid, val))

            if calc(mid):
                r = mid
            else:
                l = mid + 1

        return l
