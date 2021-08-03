class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        l = len(arr)
        tup = c.most_common(len(c))
        i = 0
        while l > len(arr) / 2:
            l -= tup[i][1]
            i += 1

        return i
