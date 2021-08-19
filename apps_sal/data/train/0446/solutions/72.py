class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        res = len(counter)
        for key in list(sorted(counter.keys(), key=lambda x: counter[x])):
            freq = counter[key]
            if k >= freq:
                res -= 1
                k -= freq
        return res
