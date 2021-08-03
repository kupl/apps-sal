from collections import defaultdict
from functools import reduce


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        mod = (1 << 63 - 1)
        A = [ord(c) - ord('a') for c in S]

        def find_dup_of_length(L):
            p = pow(26, L, mod)
            h = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = defaultdict(list)
            seen[h].append(0)

            for i in range(L, len(S)):
                h = (h * 26 + A[i] - p * A[i - L]) % mod
                for start in seen[h]:
                    if S[start:start + L] == S[i - L + 1:i + 1]:
                        return start

                seen[h].append(i - L + 1)

        start = 0
        length = 0
        low, high = 1, len(S)
        while low < high:
            mid = low + (high - low) // 2
            pos = find_dup_of_length(mid)
            if pos is not None:
                start = pos
                length = mid
                low = mid + 1
            else:
                high = mid

        return S[start:start + length]
