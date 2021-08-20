class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        if people[0] >= limit:
            return 0
        res = [0]
        (i, j) = (0, len(people) - 1)
        num_people = 0
        while i <= j:
            if res[-1] + people[j] <= limit and num_people < 2:
                res[-1] += people[j]
                j -= 1
                num_people += 1
            elif res[-1] + people[i] <= limit and num_people < 2:
                res[-1] += people[i]
                i += 1
                num_people += 1
            else:
                res.append(0)
                num_people = 0
        return len(res)
