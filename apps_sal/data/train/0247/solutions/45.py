class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        def get_shortest(array):
            shortest = [float('infinity') for _ in range(len(arr))]
            prefix_pos = {}
            prefix_sum = 0
            for i in range(len(array)):
                prefix_sum += array[i]
                if prefix_sum == target:
                    if i == 0:
                        shortest[i] = i + 1
                    else:
                        shortest[i] = min(shortest[i - 1], i + 1)
                elif prefix_sum - target in prefix_pos:
                    shortest[i] = i - prefix_pos[prefix_sum - target] + 1
                shortest[i] = min(shortest[i - 1], shortest[i])
                prefix_pos[prefix_sum] = i + 1
            return shortest
        left = get_shortest(arr)
        right = get_shortest(arr[::-1])[::-1]
        res = float('infinity')
        for i in range(len(left) - 1):
            res = min(res, left[i] + right[i + 1])
        if res == float('infinity'):
            return -1
        return res
