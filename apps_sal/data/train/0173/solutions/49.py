class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_cnt = {}
        for n in arr:
            if not n % k in remainder_cnt:
                remainder_cnt[n % k] = 0
            remainder_cnt[n % k] += 1

        for i in remainder_cnt:
            if i == 0 or i == k / 2:
                if remainder_cnt[i] % 2 != 0:
                    return False
            elif not k - i in remainder_cnt or remainder_cnt[i] != remainder_cnt[k - i]:
                # print(remainder_cnt,i)
                return False

        return True
