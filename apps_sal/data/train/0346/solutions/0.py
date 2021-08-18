class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        edge = []
        res = 0
        count = 0
        for i in nums:
            if i % 2:
                edge.append(count + 1)
                count = 0
            else:
                count += 1
        edge.append(count + 1)
        if len(edge) - 1 < k:
            return 0
        else:
            for i in range(len(edge) - k):
                res += edge[i] * edge[i + k]
            return res
