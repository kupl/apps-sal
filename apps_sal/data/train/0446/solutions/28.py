class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if not arr:
            return 0

        dic = collections.defaultdict(int)
        for n in arr:
            dic[n] += 1

        l = []

        for key, val in dic.items():
            l.append([key, val])

        l.sort(key=lambda x: x[1])
        # print(l)
        count = len(l)

        for i in range(len(l)):
            if k == 0:
                break
            n = min(k, l[i][1])
            l[i][1] -= n
            k -= n
            if l[i][1] == 0:
                count -= 1
                i -= 1

        # print(l)
        return count
