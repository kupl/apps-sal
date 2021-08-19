class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        s = 0
        res = 0
        for a in satisfaction:
            s += a
            if s <= 0:
                break
            res += s
        return res
    '\n    将所有大于的的前缀子串都加上\n    大数尽可能多家几次，所以先倒序\n    到当前位置的前缀和\n    一直计算前缀和，直到前缀和<=0  结束\n    [9, 8, 5, 2, 1, -1]\nsum = 9 * 4 + 8 * 3 + 2 * 3 + 1 * 2 + -1 * 1\n<=>\nsum += 9\nsum += (9 + 8 = 17)\nsum += (17 + 2 = 19)\nsum += (19 + 1 = 20)\nsum += (20 – 1 = 19)\n    '
