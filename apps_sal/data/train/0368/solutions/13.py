from collections import deque


class Solution:

    def ComputeLikeTime(self, prepared_dishes):
        like_time = 0
        dish_index = 1
        for satisfaction in prepared_dishes:
            like_time += dish_index * satisfaction
            dish_index += 1
        return like_time

    def maxSatisfaction(self, satisfaction):
        satisfaction = sorted(satisfaction, reverse=True)
        prepared_dishes = deque()
        max_satisfaction = 0
        for val in satisfaction:
            prepared_dishes.appendleft(val)
            satisfaction = self.ComputeLikeTime(prepared_dishes)
            if satisfaction > max_satisfaction:
                max_satisfaction = satisfaction
        return max_satisfaction
