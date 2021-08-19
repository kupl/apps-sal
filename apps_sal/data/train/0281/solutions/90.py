class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        ls = [ord(j) - ord(i) for i, j in zip(s, t)]
        for i in range(n):
            if ls[i] < 0:
                ls[i] = 26 + ls[i]
        d = {}
        ans = 0
        # print(ls)
        for i in ls:
            if i == 0:
                continue
            if i not in d:
                ans = max(ans, i)
                d[i] = 1
            else:
                ans = max(26 * d[i] + i, ans)
                d[i] += 1
            if ans > k:
                # print(ans, k, d)
                return False
        return True
