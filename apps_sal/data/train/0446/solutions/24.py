class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        s = sorted(arr, key=lambda x: (c[x], x))
        print(s)
        return len(set(s[k:]))
