class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        for num in arr:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1

        l = [v for k, v in sorted(dic.items(), key=lambda item: item[1])]

        while len(l) > 0 and l[0] <= k:
            k -= l.pop(0)

        return len(l)
