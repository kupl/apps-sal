class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        tail = collections.Counter()

        maxi = 1
        for n in arr:
            if n - difference in tail:
                maxi = max(maxi, tail[n - difference] + 1)
                tail[n] = tail[n - difference] + 1
            else:
                tail[n] = 1
            # print(tail, n, maxi)
        return maxi
