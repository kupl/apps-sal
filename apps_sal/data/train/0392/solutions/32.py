class Solution:

    def numWays(self, s: str) -> int:
        n = s.count('1')
        M = 1000000007
        if not n:
            return (len(s) - 2) * (len(s) - 1) // 2 % M
        if n % 3:
            return 0
        n //= 3
        i = 0
        cnt = 0
        while i < len(s):
            if s[i] == '1':
                cnt += 1
                if cnt == n:
                    break
            i += 1
        j = len(s) - 1
        cnt = 0
        while j >= 0:
            if s[j] == '1':
                cnt += 1
                if cnt == n:
                    break
            j -= 1
        k = i + 1
        while k < len(s) and s[k] == '0':
            k += 1
        l = j - 1
        while l > 0 and s[l] == '0':
            l -= 1
        return (j - l) * (k - i) % M
