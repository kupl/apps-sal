class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        count = 0
        (i, j) = (0, len(people) - 1)
        while 0 <= i < j < len(people):
            while 0 <= i < j < len(people) and people[i] + people[j] > limit:
                j -= 1
                count += 1
            i += 1
            j -= 1
            count += 1
        if i == j:
            count += 1
        return count
