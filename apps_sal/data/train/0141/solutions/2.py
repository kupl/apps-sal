class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people, reverse=True)
        i = 0
        j = len(people) - 1
        n = 0
        while True:
            if i >= j:
                break
            n += 1
            w1 = people[i]
            i += 1
            rem = limit - w1
            if rem >= people[j]:
                j -= 1

        if i == j:
            n += 1

        return n
