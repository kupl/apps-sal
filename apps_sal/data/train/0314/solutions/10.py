class Solution:
    def numSub(self, s: str) -> int:
        n = len(s)
        i = 0

        count = 0
        while (i < n):
            if s[i] == '1':
                seq = 0
                while (i < n) and (s[i] == '1'):
                    seq += 1
                    i += 1
                count += seq * (seq + 1) // 2

            else:
                i += 1

        print(count % (10**9 + 7))

        return count % (10**9 + 7)
