class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = collections.Counter(arr)
        cnt = sorted(cnt.values())
        while cnt:
            num = cnt.pop(0)
            k -= num
            if k < 0:
                return len(cnt)+1
            elif k == 0:
                return len(cnt)

