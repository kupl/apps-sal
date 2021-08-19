class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        count = 0
        while i <= j:
            if people[i] + people[j] > limit:
                count = count + 1
                j = j - 1
            else:
                count = count + 1
                i = i + 1
                j = j - 1
        return count
