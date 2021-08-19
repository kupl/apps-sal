class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        fruit_types = collections.Counter()
        max_fruit = 0

        start_idx = 0
        end_idx = 0

        # Move end pointer forward
        while end_idx < len(tree):
            fruit_types[tree[end_idx]] += 1

            # Move start pointer forward
            while len(fruit_types) > 2:
                fruit_types[tree[start_idx]] -= 1
                if fruit_types[tree[start_idx]] == 0:
                    del fruit_types[tree[start_idx]]
                start_idx += 1

            max_fruit = max(max_fruit, sum(fruit_types.values()))

            end_idx += 1

        return max_fruit
