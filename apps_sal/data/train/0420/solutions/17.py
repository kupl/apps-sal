class Solution:

    def findTheLongestSubstring1(self, s: str) -> int:

        def check(L, R, cnt_memo):
            if L > R:
                return 0
            elif (L, R) in memo:
                return memo[L, R]
            elif all((v % 2 == 0 for v in list(cnt_memo.values()))):
                return R - L + 1
            else:
                old_L = L
                new_memo = {k: v for (k, v) in list(cnt_memo.items())}
                while s[L] not in 'aeiou':
                    L += 1
                new_memo[s[L]] -= 1
                if new_memo[s[L]] == 0:
                    del new_memo[s[L]]
                res1 = check(L + 1, R, new_memo)
                L = old_L
                old_R = R
                new_memo = {k: v for (k, v) in list(cnt_memo.items())}
                while s[R] not in 'aeiou':
                    R -= 1
                new_memo[s[R]] -= 1
                if new_memo[s[R]] == 0:
                    del new_memo[s[R]]
                res2 = check(L, R - 1, new_memo)
                R = old_R
                res = max(res1, res2)
                memo[L, R] = res
                return res
        cnt_memo = collections.Counter(s)
        cnt_memo = {k: v for (k, v) in list(cnt_memo.items()) if k in 'aeiou'}
        memo = dict()
        res = check(0, len(s) - 1, cnt_memo)
        return res

    def findTheLongestSubstring(self, s: str) -> int:
        res = 0
        curr = 0
        memo = dict()
        memo[0] = -1
        for (i, c) in enumerate(s):
            if c == 'a':
                curr ^= 1
            elif c == 'e':
                curr ^= 2
            elif c == 'i':
                curr ^= 4
            elif c == 'o':
                curr ^= 8
            elif c == 'u':
                curr ^= 16
            if curr in memo:
                res = max(res, i - memo[curr])
            else:
                memo[curr] = i
        return res
        return
