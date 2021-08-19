class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        new = sorted(people)
        (i, j) = (0, len(people) - 1)
        res = 0
        while i <= j:
            if new[j] + new[i] <= limit:
                i += 1
            j -= 1
            res += 1
        return res
