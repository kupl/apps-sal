from collections import defaultdict


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        mod = 10 ** 9 + 7

        def get_rep(l: int) -> str:
            mp = defaultdict(list)  # key: hash_code, value: list of start indexes of substrings
            a = 13
            sofar = 0
            factor = 1
            for i in range(l):
                sofar = (sofar * a + ord(S[i])) % mod
                factor = (factor * a) % mod
            mp[sofar].append(0)
            for i in range(l, len(S)):
                sofar = (sofar * a + ord(S[i]) - factor * ord(S[i - l])) % mod
                if sofar in mp:
                    for j in mp[sofar]:
                        if S[j: j + l] == S[i - l + 1: i + 1]:
                            return S[i - l + 1: i + 1]
                mp[sofar].append(i - l + 1)
            return None

        low, high = 0, len(S) - 1
        ans = None
        while low <= high:
            mid = (low + high) // 2
            res = get_rep(mid)
            if res is None:
                high = mid - 1
            else:
                ans = res
                low = mid + 1
        return ans if ans is not None else ''
