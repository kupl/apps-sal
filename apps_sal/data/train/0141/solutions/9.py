class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if not people:
            return 0

        people = sorted(people)

        left = 0
        right = len(people) - 1
        board_cnt = 0

        while left <= right:
            if left == right:
                board_cnt += 1
                break

            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                board_cnt += 1
            else:
                right -= 1
                board_cnt += 1

        return board_cnt
