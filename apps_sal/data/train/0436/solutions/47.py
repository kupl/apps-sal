class Solution:
    def minDays(self, n: int) -> int:
        q = [n]
        v = set()
        steps = 0
        while len(q) > 0:
            newq = []
            for node in q:
                if node == 0: return steps
                v.add(node)
                if node % 3 == 0 and node // 3 not in v: newq.append(node // 3)
                if node % 2 == 0 and node // 2 not in v: newq.append(node // 2)
                if node - 1 not in v: newq.append(node - 1)
            q = newq
            steps += 1
        return -1
