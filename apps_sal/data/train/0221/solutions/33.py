class Solution:
    def longestDupSubstring(self, S: str) -> str:

        def code(t):
            return ord(t) - ord('a') + 1

        def check(length):
            seen = collections.defaultdict(list)

            MOD = 10 ** 9 + 7
            P = 113
            INV_P = pow(P, MOD - 2, MOD)

            h = 0
            power = 1
            '''
            h1 = s[0]p^0+s[1]p^1+s[2]p^2 +...+s[length-1]p^(length-1)
            move next:
            h2 = s[1]p^0+s[2]p^1+s[3]p^2 +...+s[length]p^(length-1)
            
            h2 = (h1 - S[i-length+1])*INV_P % MOD
            
            '''
            for i, x in enumerate(S):
                h = (h + power * code(x)) % MOD
                if i < length - 1:
                    power = power * P % MOD
                else:
                    # start: i-(length-1)
                    if h in seen:
                        for j in seen[h]:
                            if S[i - (length - 1):i + 1] == S[j:j + length]:
                                return S[j:j + length], True
                    seen[h].append(i - (length - 1))
                    h = (h - code(S[i - (length - 1)])) * INV_P % MOD

            return '', False

        res = ''
        l, r = 1, len(S) - 1
        while l <= r:
            mid = (l + r) // 2
            sub, is_check = check(mid)
            if is_check:
                res = sub
                l = mid + 1
            else:
                r = mid - 1

        return res
