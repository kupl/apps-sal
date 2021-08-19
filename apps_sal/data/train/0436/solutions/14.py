class Solution:

    def minDays(self, n: int) -> int:
        (frontier, res) = ([n], 0)
        while frontier:
            new_frontier = set()
            for el in frontier:
                if el == 1:
                    return res + 1
                new_frontier.add(el - 1)
                if el % 2 == 0:
                    new_frontier.add(el // 2)
                if el % 3 == 0:
                    new_frontier.add(el // 3)
            res += 1
            frontier = list(new_frontier)
