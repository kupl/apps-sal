class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        n = len(arr)
        ans = 1
        hmap = {arr[0]: 1}
        for i in range(1, n):
            hmap[arr[i]] = 1
            if arr[i] - diff in hmap:
                hmap[arr[i]] = max(hmap[arr[i]], hmap[arr[i] - diff] + 1)
            ans = max(ans, hmap[arr[i]])
        return ans
