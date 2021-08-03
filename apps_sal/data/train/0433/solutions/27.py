class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        a = [0] * (n + 1)
        for i in range(1, n + 1):
            a[i] = arr[i - 1] + a[i - 1]
        cnt = 0
        for i in range(k, n + 1):
            res = a[i] - a[i - k]
            if(res / k >= threshold):
                cnt += 1
        return cnt
