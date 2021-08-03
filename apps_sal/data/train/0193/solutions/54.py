class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counter = collections.Counter(arr)
        cur = 0
        ans = 0
        for num in sorted(list(counter.values()), reverse=True):
            cur += num
            ans += 1
            if cur >= n // 2:
                return ans
