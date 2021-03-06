class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        numsdict = {}
        for i in arr:
            numsdict[i] = numsdict.get(i, 0) + 1
        sortarr = sorted(numsdict.values(), reverse=True)
        count = 0
        i = 0
        while 2 * count < len(arr):
            count += sortarr[i]
            i += 1
        return i
