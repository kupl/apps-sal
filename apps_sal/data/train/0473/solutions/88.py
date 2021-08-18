class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefixSum = [0] * (len(arr) + 1)
        for i, v in enumerate(arr):
            prefixSum[i + 1] = prefixSum[i] ^ v

        ans = 0
        for i in range(1, len(prefixSum)):
            for j in range(i + 1, len(prefixSum)):
                for k in range(j, len(prefixSum)):
                    if prefixSum[i - 1] ^ prefixSum[j - 1] == prefixSum[j - 1] ^ prefixSum[k]:
                        ans += 1

        return ans
