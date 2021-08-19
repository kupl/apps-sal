from collections import Counter


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        temp = sorted([(v, k) for (k, v) in list(cnt.items())])
        curr = 0
        for i in range(1, len(temp) + 1):
            curr += temp[-i][0]
            if curr >= len(arr) / 2:
                return i
