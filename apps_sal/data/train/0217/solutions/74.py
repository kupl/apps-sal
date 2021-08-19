class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        (ans, frontier) = (set(), set())
        for n in A:
            frontier = {x | n for x in frontier if x | n != -1}
            frontier.add(n)
            ans |= frontier
        return len(ans)
