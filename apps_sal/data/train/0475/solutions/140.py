class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        pq = []

        for i in range(len(nums)):
            tot = 0
            for j in range(i, len(nums)):
                tot += nums[j]

                if len(pq) == right:
                    heappushpop(pq, -tot)
                else:
                    heappush(pq, -tot)

        sums = 0
        for i in range(right - left + 1):
            sums += heappop(pq)

        return -sums % (10**9 + 7)
