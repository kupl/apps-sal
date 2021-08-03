class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def getPower(num):
            if num == 1:
                return 1
            count = 0
            while num != 1:
                if num % 2 == 0:
                    num = num / 2
                    count += 1
                else:
                    num = 3 * num + 1
                    count += 1
            return count
        dic = {}
        for i in range(lo, hi + 1):
            dic[i] = getPower(i)
        dic = {k: v for k, v in sorted(dic.items())}
        dic = {k: v for k, v in sorted(list(dic.items()), key=lambda item: item[1])}
        return list(dic.keys())[k - 1]
