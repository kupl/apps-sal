class Solution:

    def queryString(self, S: str, M: int) -> bool:
        count = defaultdict(int)
        N = len(S)

        def f(ss):
            ans = 0
            nn = len(ss) - 1
            for ch in ss:
                if ch == '1':
                    ans += 1 << nn
                nn -= 1
            return ans
        cnt = 0
        for n1 in range(N):
            for n2 in range(n1, N):
                if n2 - n1 < 32:
                    val = f(S[n1:n2 + 1])
                    if val >= 1 and val <= M and (count[val] == 0):
                        cnt += 1
                        count[val] = 1
        if cnt == M:
            return True
        return False
