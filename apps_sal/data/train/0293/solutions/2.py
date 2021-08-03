class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        l, dic = len(tasks), {}
        for c in tasks:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        m, a = max(dic.values()), 0
        for c in dic:
            if dic[c] == m:
                a += 1
        return max(l, (m - 1) * (n + 1) + a)
