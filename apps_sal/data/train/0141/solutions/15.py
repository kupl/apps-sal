class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # start at ends and move inward

        people.sort()
        start = 0
        end = len(people) - 1
        ans = 0

        while start <= end:
            ans += 1
            if people[start] + people[end] <= limit:
                start += 1
            end -= 1

        return ans
