class Solution:
    def minDays(self, n: int) -> int:
        if n == 0:
            return 0

        q = set([n])
        level = 0

        while q:
            nq = set()
            level += 1

            for item in q:
                if item == 1:
                    return level

                nq.add(item - 1)

                if item % 2 == 0:
                    nq.add(item // 2)

                if item % 3 == 0:
                    nq.add(item // 3)

            q = nq
