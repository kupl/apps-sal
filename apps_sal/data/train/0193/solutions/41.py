class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        objective = len(arr) // 2
        res = ret = 0
        c = collections.Counter(arr)
        for k, v in c.most_common():
            res += v
            ret += 1
            if res >= objective:
                break
        return ret
