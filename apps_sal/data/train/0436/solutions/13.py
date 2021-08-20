class Solution:

    def minDays(self, n: int) -> int:
        q = set([n])
        level = 1
        while q:
            new_q = set()
            for node in q:
                if node - 1 == 0:
                    return level
                new_q.add(node - 1)
                if node % 2 == 0:
                    new_q.add(node // 2)
                if node % 3 == 0:
                    new_q.add(node // 3)
            level += 1
            q = new_q
