class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        res = -1

        lenMap = dict()
        cntMap = collections.defaultdict(lambda: 0)

        for i, x in enumerate(arr):
            left = 0
            right = 0

            if x - 1 in lenMap:
                left = lenMap[x - 1]
                cntMap[left] -= 1
            if x + 1 in lenMap:
                right = lenMap[x + 1]
                cntMap[right] -= 1

            newLen = 1 + left + right
            lenMap[x] = lenMap[x - left] = lenMap[x + right] = newLen
            cntMap[newLen] += 1

            if cntMap[m] != 0:
                res = i + 1

        return res
