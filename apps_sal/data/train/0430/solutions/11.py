class Solution:
    def distinctSubseqII(self, S: str) -> int:
        ln = 1000000007
        if len(S) == 0:
            return 0
        l = [1]

        for i in range(1, len(S)):
            cur = 0
            for j in range(i - 1, -1, -1):
                cur += l[j]
                if S[i] == S[j]:
                    break
                if j == 0:
                    cur += 1

            l.append(cur % ln)

        res = 0
        for i in l:
            res += i
            res %= ln

        return res
