class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        sums = [0 for i in range(len(counter))]
        curr = 0
        half = len(arr) // 2
        if len(arr) % 2 == 1:
            half += 1
        res = len(counter)
        for (i, key) in enumerate(sorted(counter.keys(), key=lambda x: counter[x], reverse=True)):
            curr += counter[key]
            if curr >= half:
                res = min(res, i + 1)
        return res
