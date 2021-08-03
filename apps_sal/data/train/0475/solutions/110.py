class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        s = [0]
        for x in nums:
            s.append(s[-1] + x)
        n = len(nums)
        q = [(x, i, i) for i, x in enumerate(nums)]
        heapq.heapify(q)
        i = 1
        ans = 0
        while i <= right:
            x, j, k = heapq.heappop(q)
            if i >= left:
                ans += x
            if k > 0:
                k -= 1
                y = s[j + 1] - s[k]
                heapq.heappush(q, (y, j, k))
            i += 1
        return ans % (10 ** 9 + 7)
