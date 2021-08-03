class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        low = 0
        up = len(people) - 1
        boats = 0

        while(low <= up):
            if up - 1 >= low and people[up] + people[up - 1] <= limit:
                up -= 2
                boats += 1
            elif up != low and people[up] + people[low] <= limit:
                up -= 1
                low += 1
                boats += 1
                added = True
            else:
                up -= 1
                boats += 1

        return boats
