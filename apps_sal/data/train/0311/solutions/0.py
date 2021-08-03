class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        if not ratings:
            return 0

        total, pre, decrease = 1, 1, 0
        for i in range(1, len(ratings)):
            if ratings[i] >= ratings[i - 1]:
                if decrease > 0:
                    total += (1 + decrease) * decrease // 2
                    if pre <= decrease:
                        total += decrease + 1 - pre
                    decrease, pre = 0, 1
                if ratings[i] == ratings[i - 1]:
                    total += 1
                    pre = 1
                else:
                    pre += 1
                    total += pre
            else:
                decrease += 1

        if decrease > 0:
            total += (1 + decrease) * decrease // 2
            if pre <= decrease:
                total += decrease + 1 - pre
        return total
