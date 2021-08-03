class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        c = Counter(arr)
        s = sorted(arr, key=lambda x: (c[x], x))
        return len(set(s[k:]))
