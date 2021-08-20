class Solution:

    def maxDistToClosest(self, seats: List[int]) -> int:
        seat_max_space = 0
        max_dis = 0
        for (i, s) in enumerate(seats):
            if s == 0:
                j = i - 1
                min_left = j
                left_seat_found = False
                while j >= 0:
                    if seats[j] == 1:
                        min_left = j
                        left_seat_found = True
                        break
                    j -= 1
                k = i
                min_right = k + 1
                right_seat_found = False
                while k < len(seats):
                    if seats[k] == 1:
                        min_right = k
                        right_seat_found = True
                        break
                    k += 1
                if right_seat_found is False and left_seat_found is False:
                    return len(seats) - 1
                if right_seat_found is False:
                    min_right = min_left
                if left_seat_found is False:
                    min_left = min_right
                closer = abs(min(i - min_left, min_right - i))
                seat_max_space = max(seat_max_space, closer)
        print(seat_max_space)
        return seat_max_space
