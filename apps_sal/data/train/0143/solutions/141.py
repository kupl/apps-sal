class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        max_count = pair_count = last_count = 0
        fruit_1 = fruit_2 = last_fruit = None
        for fruit_type in tree:
            if fruit_type == fruit_1:
                pair_count += 1
                if fruit_type == last_fruit:
                    last_count += 1
                else:
                    last_fruit = fruit_type
                    last_count = 1
            elif fruit_type == fruit_2:
                pair_count += 1
                if fruit_type == last_fruit:
                    last_count += 1
                else:
                    last_fruit = fruit_type
                    last_count = 1
            elif fruit_1 == None:
                fruit_1 = last_fruit = fruit_type
                last_count = 1
                pair_count += 1
            elif fruit_2 == None:
                fruit_2 = last_fruit = fruit_type
                last_count = 1
                pair_count += 1
            else:
                fruit_1 = last_fruit
                fruit_2 = last_fruit = fruit_type
                max_count = max(max_count, pair_count)
                pair_count = last_count + 1
                last_count = 1
        return max(max_count, pair_count)
