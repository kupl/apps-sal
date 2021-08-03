class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks:
            return 0
        counts = {}
        for i in tasks:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        M = max(counts.values())
        Mct = sum([1 for i in counts if counts[i] == M])
        return max(len(tasks), (M - 1) * (n + 1) + Mct)
