class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = dict()
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for (key, value) in sorted(d.items(), key=lambda item: item[1]):
            if k >= value:
                k -= value
                del d[key]
            else:
                break
        return len(d)
