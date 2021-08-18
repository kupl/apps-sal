class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        s = set()
        res = 0
        for i in range(0, len(text), 1):
            for j in range(i + 1, len(text), 2):
                mid = (i + j - 1) // 2
                t1 = text[i:mid + 1]
                t2 = text[mid + 1:j + 1]

                if t1 == t2 and t1 not in s:
                    s.add(text[i:mid + 1])
                    res += 1

        return len(s)

        n = len(s)
        dp = [0 for i in range(n)]

        dp[0] = ord(s[0]) - ord('a')

        pw = [0] * (n + 1)

        pw[0] = 1

        curr = 26

        for i in range(1, n):
            dp[i] = dp[i - 1] + curr * (ord(s[i]) - ord('a'))
            pw[i] = curr
            curr = curr * 26

        pw[-1] = curr

        st = set()

        for i in range(n):
            for j in range(i + 1, n, 2):

                mid = (j + i) // 2

                if i != 0:
                    x1 = dp[mid] - dp[i - 1]
                else:
                    x1 = dp[mid]

                x2 = dp[j] - dp[mid]

                if x2 == x1 * (pw[mid - i + 1]):
                    if s[i:mid + 1] == s[mid + 1:j + 1]:
                        st.add(s[i:j + 1])
        return len(st)
