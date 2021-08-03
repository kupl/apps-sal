class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def bitsoncount(x):
            return bin(x).count('1')

        ans = 0
        n = len(s)
        seen = defaultdict(int)
        for m in range(1 << n):
            if (bitsoncount(m) <= ans):
                continue
            prev = 0
            count = 0
            for i in range(n):
                if m & (1 << i):
                    sub = s[prev:i + 1]
                    prev = i + 1
                    if sub not in seen:
                        seen[sub] += 1
                        count += 1

            ans = max(ans, count)
            seen.clear()

        return ans
