class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        ordered_satis = sorted(satisfaction)
        nums = len_num = len(ordered_satis)
        max_satis = 0
        while len_num > 0:
            tem_max = 0
            for i, j in enumerate(ordered_satis):
                if nums - len_num > i:
                    continue
                tem_max += (i + 1 + len_num - nums) * j
            max_satis = max(max_satis, tem_max)
            len_num -= 1
        return max_satis
