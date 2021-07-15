class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        run = [0]
        for i in range(len(arr)):
            run.append(run[-1] + arr[i])
        res = 0
        for i in range(k, len(arr) + 1):
            if (run[i] - run[i - k]) / k >= threshold:
                res += 1
        return res
