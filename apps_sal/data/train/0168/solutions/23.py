class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        cnt = Counter()

        for c in s:
            cnt[c] += 1

        single_nums = 0

        for key in cnt:
            if cnt[key] % 2 == 1:
                single_nums += 1

        if k < single_nums:
            return False

        return True
