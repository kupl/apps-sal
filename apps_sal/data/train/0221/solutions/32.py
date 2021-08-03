from collections import defaultdict


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        l, h = 2, len(S) - 1
        res = ''
        while l <= h:
            m = l + (h - l) // 2
            cand = self.find_dup_substr_len_k(S, m)
            if cand:
                res = cand
                l = m + 1
            else:
                h = m - 1
        return res

    def find_dup_substr_len_k(self, s, k):
        MOD = (1 << 63) - 1
        BASE = 26
        D = pow(BASE, k - 1, MOD)
        hash_val = 0
        seen = defaultdict(set)

        for i in range(len(s)):
            # update the sliding hash value
            if i >= k:
                char_offset = ord(s[i - k]) - ord('a')
                hash_val = (hash_val - char_offset * D) % MOD
            char_offset = ord(s[i]) - ord('a')
            hash_val = (hash_val * BASE + char_offset) % MOD

            # check hash collision and return string if duplicate found
            if i >= k - 1:
                if hash_val in seen:
                    cand_i = s[i - k + 1:i + 1]
                    for j in seen[hash_val]:
                        cand_j = s[j - k + 1:j + 1]
                        if cand_i == cand_j:
                            return cand_i
                seen[hash_val].add(i)
        return ''
