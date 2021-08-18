class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        from collections import defaultdict
        self.ans = 1

        def get(s, l, n):
            if n == len(s):
                dic = defaultdict(int)
                for i in l:
                    dic[i] += 1
                z = True
                for i in dic:
                    if dic[i] > 1:
                        z = False
                        break
                if z:
                    self.ans = max(self.ans, len(l))
                return
            i = n
            cur = ''
            for j in range(i, len(s)):
                cur += s[j]
                get(s, l + [cur], j + 1)

        get(s, [], 0)
        return self.ans
