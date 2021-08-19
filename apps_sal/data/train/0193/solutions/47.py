class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        c = collections.Counter(arr)
        n = len(arr)
        res = 0
        count = 0
        for (c, v) in c.most_common():
            count += v
            res += 1
            if count >= n // 2:
                break
        return res
