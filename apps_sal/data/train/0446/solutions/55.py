class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        keys = dic.keys()
        keys = sorted(keys, key=lambda a: dic[a])
        for index in range(len(keys)):
            if k == 0:
                return len(keys)-index
            elif k-dic[keys[index]] < 0:
                return len(keys)-index
            else:
                k -= dic[keys[index]]
        return 0
