import collections
import numpy as np


class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(range(len(position)), key=lambda i: position[i])

        def calc_finish_time(car):
            return (target - position[cars[car]]) / speed[cars[car]]
        fleets = 0
        next_finish_time = -1
        for car in range(len(cars) - 1, -1, -1):
            finish_time = max(calc_finish_time(car), next_finish_time)
            if finish_time != next_finish_time:
                fleets += 1
            next_finish_time = finish_time
        return fleets
