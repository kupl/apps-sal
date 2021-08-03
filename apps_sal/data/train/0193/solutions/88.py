class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = collections.defaultdict(int)
        for i in arr:
            d[i] += 1
        res = len(arr)
        orig = len(arr)
        count = 0

        freq = [(d[i], i) for i in d]
        freq.sort(reverse=True)
        count = 0
        for i in freq:
            res -= i[0]
            count += 1
            if res <= orig // 2:
                return count
        return -1
