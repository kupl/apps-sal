class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # premin[i] is the min len of subarr with sum in arr[:i+1]
        premin = [float('inf')] * len(arr)
        l, cur, res = 0, 0, float('inf')
        for r, num in enumerate(arr):
            if r > 0: premin[r] = premin[r - 1]
            cur += num
            while cur > target:
                cur -= arr[l]
                l += 1
            if cur == target:
                size = r - l + 1
                if l > 0: res = min(res, size + premin[l - 1])
                premin[r] = min(premin[r], size)
        return res if res < float('inf') else -1
