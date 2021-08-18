class Solution:
    def findLengthOfShortestSubarray(self, a: List[int]) -> int:
        n = len(a)
        if all(a[i] >= a[i - 1] for i in range(1, n)):
            return 0
        d = {x: i + 1 for i, x in enumerate(sorted(set(a)))}
        a = [d[x] for x in a]
        last = [0] * (len(d) + 1)
        prev = -1
        for i, x in enumerate(a):
            if x < prev:
                break
            last[x] = i + 1
            prev = x

        for i in range(1, len(d) + 1):
            if last[i] == 0:
                last[i] = last[i - 1]

        ans = last[-1]
        prev = 1e100
        for i, x in enumerate(a[::-1]):
            if prev < x:
                break
            print(prev, x, last[x], i)
            ans = max(ans, i + 1 + last[x])
            prev = x
        return n - ans
