class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        cnt = defaultdict(int)

        for i in range(n):
            now = ''
            se = set()

            for j in range(maxSize):
                if i + j >= n:
                    break

                now += s[i + j]
                se.add(s[i + j])

                if len(se) <= maxLetters and len(now) >= minSize:
                    cnt[now] += 1

        ans = 0

        for v in cnt.values():
            ans = max(ans, v)

        return ans
