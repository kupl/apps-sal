class Solution:

    def maskPII(self, S: str) -> str:
        N = len(S)
        if '@' in S:
            S = S.lower()
            (first, rest) = S.split('@')
            return first[0] + '*' * 5 + first[-1] + '@' + rest
        else:
            digits = ''.join((c for c in S if c.isdigit()))
            a = []
            if len(digits) > 10:
                a.append('+' + '*' * (len(digits) - 10))
            a.append('***')
            a.append('***')
            a.append(digits[-4:])
            return '-'.join(a)
