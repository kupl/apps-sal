class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K >= 2:
            return ''.join(sorted(S))

        length = len(S)
        S = S + S
        i, j, k = 0, 1, 0
        while j + k < len(S) and k < length:
            if S[i + k] == S[j + k]:
                k += 1
                continue
            elif S[i + k] < S[j + k]:
                j = j + k + 1
            else:
                i = max(i + k + 1, j)
                j = i + 1
            k = 0
        return S[i: i + length]
