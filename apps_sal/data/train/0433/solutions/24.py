class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0

        n = len(arr)
        start = 0
        end = 0

        presum = [0]

        for num in arr:
            presum.append(presum[-1] + num)

        for i in range(0, n - k + 1):

            if (presum[i + k] - presum[i]) / k >= threshold:
                # print(arr[start:end])
                ans += 1

        return ans
