class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        first_index = 0
        second_index = len(people) - 1
        ans = 0
        while first_index <= second_index:
            if people[first_index] + people[second_index] <= limit:
                second_index -= 1
            first_index += 1
            ans += 1
        return ans
