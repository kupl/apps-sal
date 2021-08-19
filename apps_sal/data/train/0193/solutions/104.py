class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        h = {}
        for el in arr:
            if el not in h:
                h[el] = 0
            h[el] += 1
        tmp = []
        for key in list(h.keys()):
            tmp.append(h[key])
        tmp.sort()
        count = 0
        size = 0
        for i in range(len(tmp) - 1, -1, -1):
            size += tmp[i]
            count += 1
            if size >= math.ceil(len(arr) / 2):
                break
        return count
