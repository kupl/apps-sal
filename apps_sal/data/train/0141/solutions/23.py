class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        i = 0
        j = len(people) - 1
        total = 0
        while i <= j:
            if i == j:
                total += 1
                i += 1
                j -= 1
            else:
                if people[i] + people[j] <= limit:
                    i += 1
                    j -= 1
                    total += 1
                else:
                    j -= 1
                    total += 1
        return total
        # print(people)
        # while i < len(people):
        #     print(i,people)
        #     if i < len(people) - 1 and people[i] + people[i+1] <= limit:
        #         print(\"two peeps\")
        #         i += 2
        #     else:
        #         print(\"one peep\")
        #         i += 1
        #     total += 1
        # return total

