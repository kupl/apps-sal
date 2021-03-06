from collections import Counter


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)
        cnt = sorted(cnt.values())
        while k > 0:
            num = cnt.pop(0)
            k -= num
        if k < 0:
            return len(cnt) + 1
        elif k == 0:
            return len(cnt)
