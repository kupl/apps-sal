class Solution:
    def numOfSubarrays(self, a: List[int], k: int, threshold: int) -> int:
        prefixSum = [0]
        for i in a:
            prefixSum.append(i + prefixSum[-1])
        return sum(prefixSum[i + k] - prefixSum[i] >= k * threshold for i in range(len(a) - k + 1))
