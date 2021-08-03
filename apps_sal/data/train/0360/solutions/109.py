class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        memo = {}
        high = sum(weights)
        low = ceil(high / D)
        best = low
        mid = low + (high - low) // 2
        memo[mid] = is_possible(weights, mid, D)
        memo[mid + 1] = is_possible(weights, mid + 1, D)

        while memo[mid] or not memo[mid + 1]:
            if high == low and high == best:
                # print(\"###\")
                # print(memo[2])
                # print(memo[3])
                return best

            # print(low)
            # print(high)
            # print(mid)
            # print(\"----\")
            if not memo[mid]:  # not mid and not mid + 1, answer is higher
                low = mid

            else:  # mid and mid + 1, answer is lower
                high = mid

            mid = low + (high - low) // 2
            if mid not in memo:
                memo[mid] = is_possible(weights, mid, D)

            if mid + 1 not in memo:
                memo[mid + 1] = is_possible(weights, mid + 1, D)

        return mid + 1


def is_possible(weights, max_w, D):
    total = 0

    for i, weight in enumerate(weights):
        if weight > max_w:
            return False

        if total + weight > max_w:
            total = 0
            D -= 1

            # full before the last one is added
            if D == 0:
                return False

        total += weight

    return True
