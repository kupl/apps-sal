class Solution:

    def isPossible(self, ship_weight: int, d: int) -> bool:
        i = 0
        ships = 0
        curr_w = 0
        while i < len(self.weights):
            if ship_weight - curr_w < self.weights[i]:
                curr_w = 0
                ships += 1
                if ship_weight < self.weights[i] or ships >= d:
                    return False
            curr_w += self.weights[i]
            i += 1
        return True

    def shipWithinDays(self, weights: List[int], d: int) -> int:
        self.weights = weights
        min_w = math.ceil(sum(weights) / d)
        max_w = max(weights) * math.ceil(len(weights) / d) + 1
        while True:
            mid_w = min_w + (max_w - min_w) // 2
            if self.isPossible(mid_w, d):
                if not self.isPossible(mid_w - 1, d):
                    return mid_w
                max_w = mid_w
            else:
                min_w = mid_w
        return 0
