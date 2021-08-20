class Solution(object):

    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if not n:
            return 0
        (n, b) = (min(6, n), set())
        b.add(tuple([1] * n))
        for j in range(m):
            c = set()
            for x in b:
                for t in (tuple([(x[i] + 1) % 2 for i in range(n)]), tuple([x[i] if i % 2 == 0 else (x[i] + 1) % 2 for i in range(n)]), tuple([(x[i] + 1) % 2 if i % 2 == 0 else x[i] for i in range(n)]), tuple([(x[i] + 1) % 2 if i % 3 == 0 else x[i] for i in range(n)])):
                    if t not in c:
                        c.add(t)
            b = c
            if len(b) == 8:
                return 8
        return len(b)
