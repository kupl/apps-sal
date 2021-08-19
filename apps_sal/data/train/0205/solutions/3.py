class Solution:

    def Greedy(self, counts, zeros, ones):
        num = 0
        for (a, b) in counts:
            if a <= zeros and b <= ones:
                zeros -= a
                ones -= b
                num += 1
        return num

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        counts = [[s.count('0'), s.count('1')] for s in strs]
        res1 = self.Greedy(sorted(counts, key=lambda c: min(c[0], c[1])), m, n)
        res2 = self.Greedy(sorted(counts, key=lambda c: min(m - c[0], n - c[1]), reverse=True), m, n)
        return max(res1, res2)
