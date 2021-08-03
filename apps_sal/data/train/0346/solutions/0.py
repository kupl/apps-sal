class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # save all even subarray's length which between odds
        edge = []
        res = 0
        count = 0
        for i in nums:
            # odd
            if i % 2:
                # +1 because range from 0 to count when doing combination
                edge.append(count + 1)
                count = 0
            # even
            else:
                count += 1
        edge.append(count + 1)
        # no enough odd
        if len(edge) - 1 < k:
            return 0
        else:
            # combination
            for i in range(len(edge) - k):
                res += edge[i] * edge[i + k]
            return res
