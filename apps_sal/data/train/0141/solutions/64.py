class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        total = 0  # if len(people)%2 == 0 else 1
        people.sort()
        print(people)
        i = 0
        j = len(people) - 1
        while i <= j:
            print(j)
            if (people[i] + people[j]) > limit or i == j:
                j -= 1
                total += 1
            else:
                i += 1
                j -= 1
                total += 1

        return total
