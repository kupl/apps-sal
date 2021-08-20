class Solution:

    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        mod = 10 ** 30
        ord_a = 97

        def find_len_k_dup(k):
            hash_val = 0
            seen = set()
            for i in range(k):
                hash_val = (hash_val * 26 + (ord(S[i]) - ord_a)) % mod
            seen.add(hash_val)
            power = 26 ** k % mod
            for i in range(1, n - k + 1):
                hash_val = ((hash_val * 26 - (ord(S[i - 1]) - ord_a) * power) % mod + (ord(S[i + k - 1]) - ord_a)) % mod
                if hash_val in seen:
                    return i
                seen.add(hash_val)
            return None
        low = 0
        high = len(S)
        res = ''
        while low < high:
            mid = (low + high) // 2
            idx = find_len_k_dup(mid)
            if idx is not None:
                res = S[idx:idx + mid]
                low = mid + 1
            else:
                high = mid
        return res
