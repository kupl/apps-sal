class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefixSum = [0]
        for i in range(1, len(arr)+1):
            prefixSum.append(prefixSum[-1]+arr[i-1])
        out = 0
        prefixEven = 0
        prefixOdd = 0
        for i in range(len(prefixSum)):
            if prefixSum[i]%2 == 0:
                prefixEven += 1
                out += prefixOdd
            else:
                prefixOdd += 1
                out += prefixEven
        return out%(10**9+7)

