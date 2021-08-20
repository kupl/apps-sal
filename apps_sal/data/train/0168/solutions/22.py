class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        char_cnt = defaultdict(int)
        for char in s:
            char_cnt[char] += 1
        odd_cnt = 0
        for (char, cnt) in char_cnt.items():
            if cnt % 2 == 1:
                odd_cnt += 1
                if odd_cnt > k:
                    return False
        return True
