class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        average = sum(weights) // len(weights)
        min_capacity = max(max(weights), average)
        min_w = min_capacity
        max_w = min_w * 2
        while not enought_capacity(max_w, weights, D):
            min_w = max_w
            max_w = max_w * 2
        while True:
            mid = min_w + (max_w - min_w) // 2
            if enought_capacity(mid, weights, D):
                if mid == min_w or mid == max_w:
                    return mid
                max_w = mid
            else:
                min_w = mid + 1


def enought_capacity(capacity: int, weights: List[int], D: int):
    remain_ships = D - 1
    sum_weight = 0
    for pck_weight in weights:
        sum_weight += pck_weight
        if sum_weight > capacity:
            remain_ships -= 1
            sum_weight = pck_weight
    if remain_ships >= 0:
        return True
    return False
