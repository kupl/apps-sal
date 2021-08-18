class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        print(people)
        boats = 0
        left_index = 0
        right_index = len(people) - 1

        while left_index <= right_index:
            if people[left_index] + people[right_index] <= limit:
                left_index += 1

            boats += 1
            right_index -= 1

        return boats
