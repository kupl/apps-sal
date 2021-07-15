class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def is_edit(a, b):
            if abs(len(a) - len(b)) > 1:
                return False
            if len(a) == len(b):
                return False

            for i in range(min(len(a), len(b))):
                if a[i] != b[i]:
                    return a == b[:i] + b[i + 1:] or b == a[:i] + a[i + 1:]
            return True

        words.sort(key=lambda x: len(x))
        n = len(words)
        memo = [1 for _ in range(n)]
        ans = 1
        for i in range(n - 1, -1, -1):
            max_ = 0
            for j in range(i + 1, n):
                if is_edit(words[i], words[j]):
                    max_ = max(max_, memo[j])
            memo[i] = 1 + max_
            ans = max(memo[i], ans)
        return ans

