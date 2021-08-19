from collections import Counter


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        sz = len(arr)
        d = sorted(list(Counter(arr).items()), key=lambda x: -x[1])
        num = 0
        numElems = 0
        for e in d:
            numElems += e[1]
            if numElems < sz // 2:
                num += 1
            else:
                return num + 1
