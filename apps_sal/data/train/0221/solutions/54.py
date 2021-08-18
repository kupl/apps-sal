class Solution:
    def longestDupSubstring(self, S: str) -> str:
        res = ''
        d, q = len(set(S)), 2**63 - 1
        record = [0] * len(S)
        for i in range(len(S)):
            if i == 0:
                record[i] = ord(S[i])
            else:
                record[i] = (record[i - 1] * d + ord(S[i])) % q

        def check(mid):
            h, g = 1, set()
            for i in range(mid):
                h = h * d % q
            for i in range(len(S) - mid + 1):
                count = (record[i + mid - 1] - record[i - 1] * h) % q if i > 0 else record[i + mid - 1]
                if count not in g:
                    g.add(count)
                else:
                    return S[i:i + mid]
            return False
        l, r = 0, len(S) - 1
        while l <= r:
            mid = (l + r) // 2
            temp = check(mid)
            if temp:
                res = temp
                l = mid + 1
            else:
                r = mid - 1
        return res
