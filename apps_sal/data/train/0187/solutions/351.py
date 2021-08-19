class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        total_money = 0
        cars = [0, 0, 0, 0]
        index = 0
        max_rotations = -1
        num_rotations = 0
        max_money = 0
        while index < len(customers):
            waiting += customers[index]
            if waiting < 4:
                cars[0] = waiting
                total_money += waiting * boardingCost
                waiting = 0
            else:
                waiting -= 4
                total_money += 4 * boardingCost
                cars[0] = 4
            self.rotation(cars)
            total_money -= runningCost
            index += 1
            num_rotations += 1
            if total_money > max_money:
                max_rotations = num_rotations
                max_money = total_money
        while waiting != 0:
            if waiting < 4:
                cars[0] = waiting
                total_money += waiting * boardingCost
                waiting = 0
            else:
                waiting -= 4
                total_money += 4 * boardingCost
                cars[0] = 4
            self.rotation(cars)
            total_money -= runningCost
            num_rotations += 1
            if total_money > max_money:
                max_rotations = num_rotations
                max_money = total_money
        if max_money == 0:
            return -1
        return max_rotations

    def rotation(self, arr):
        (arr[3], arr[2], arr[1], arr[0]) = (arr[2], arr[1], arr[0], 0)
