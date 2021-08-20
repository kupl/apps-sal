class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 0
        for x in rods:
            for (diff, val) in list(dic.items()):
                dic[diff + x] = max(dic[diff + x], val)
                dic[abs(diff - x)] = max(dic[abs(diff - x)], val + min(x, diff))
        return dic[0]
