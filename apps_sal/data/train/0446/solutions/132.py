class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = sorted(collections.Counter(arr).items(), key=lambda x: x[1])
        c = 0
        for kk, v in count:
            if k >= v:
                k -= v
                c += 1
            else:
                break
        return len(count) - c
