class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []

        def power(num):
            if num == 2:
                return 1
            elif num % 2 == 0:
                return 1 + power(num // 2)
            else:
                return 1 + power(3 * num + 1)
        dic = collections.defaultdict(list)
        for i in range(lo, hi + 1):
            dic[power(i)].append(i)
        for (_, v) in sorted(dic.items()):
            res += v
        return res[k - 1]
