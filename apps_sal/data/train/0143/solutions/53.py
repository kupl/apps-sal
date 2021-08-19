class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        max_length = 0
        fruits_frequency = defaultdict(int)
        window_start = 0
        for window_end in range(0, len(tree)):
            right_fruit = tree[window_end]
            fruits_frequency[right_fruit] += 1
            while len(fruits_frequency) > 2:
                left_fruit = tree[window_start]
                fruits_frequency[left_fruit] -= 1
                if fruits_frequency[left_fruit] == 0:
                    del fruits_frequency[left_fruit]
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length
