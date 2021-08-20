class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        count = Counter(arr)
        res = 0
        s = 0
        for (key, rep) in count.most_common():
            s += 1
            res += rep
            if res >= n // 2:
                return s
