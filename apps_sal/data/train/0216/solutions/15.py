class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs) % 5 != 0:
            return -1

        min_val = 0
        cnt = {char: 0 for char in 'croak'}
        for char in croakOfFrogs:
            if char not in 'croak' or not cnt['c'] >= cnt['r'] >= cnt['o'] >= cnt['a'] >= cnt['k']:
                return -1
            cnt[char] += 1

            min_val = max(min_val, cnt['c'] - cnt['k'])

        return min_val if cnt['c'] == cnt['r'] == cnt['o'] == cnt['a'] == cnt['k'] else -1
