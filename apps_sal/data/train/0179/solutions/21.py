class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        count = 1
        prev = s[0]
        counts = []
        for l in s[1:]:
            if l == prev:
                count += 1
            else:
                counts.append([prev, count])
                count = 1
                prev = l
        counts.append([prev, count])

        @lru_cache(None)
        def opt(i, k):
            if i >= len(counts):
                return 0
            (l, c) = counts[i]
            best = 1 + (len(str(c)) if c > 1 else 0) + opt(i + 1, k)
            if k >= c:
                best = min(best, opt(i + 1, k - c))
            if c > 1 and c - 1 <= k:
                best = min(best, 1 + opt(i + 1, k - (c - 1)))
            if c > 9 and c - 9 <= k:
                best = min(best, 2 + opt(i + 1, k - (c - 9)))
            if c > 99 and c - 99 <= k:
                best = min(best, 3 + opt(i + 1, k - (c - 99)))
            j = i + 1
            while j < len(counts) and k >= 0:
                if counts[j][0] == l:
                    c += counts[j][1]
                    best = min(best, 1 + (len(str(c)) if c > 1 else 0) + opt(j + 1, k))
                    if k >= c:
                        best = min(best, opt(j + 1, k - c))
                    if c > 1 and c - 1 <= k:
                        best = min(best, 1 + opt(j + 1, k - (c - 1)))
                    if c > 9 and c - 9 <= k:
                        best = min(best, 2 + opt(j + 1, k - (c - 9)))
                    if c > 99 and c - 99 <= k:
                        best = min(best, 3 + opt(j + 1, k - (c - 99)))
                else:
                    k -= counts[j][1]
                j += 1
            return best
        return opt(0, k)
