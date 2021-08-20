class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        total_fruits = collections.defaultdict(int)
        unique_baskets = 0
        max_fruit_types = 0
        start = 0
        for end in range(len(tree)):
            cur_fruit = tree[end]
            total_fruits[cur_fruit] += 1
            if total_fruits[cur_fruit] == 1:
                unique_baskets += 1
            while unique_baskets >= 3:
                start_fruit = tree[start]
                total_fruits[start_fruit] -= 1
                if not total_fruits:
                    unique_baskets -= 1
                start += 1
            max_fruit_types = max(max_fruit_types, end - start + 1)
        return max_fruit_types


class Solution:

    def totalFruit(self, tree):
        fruit_basket = collections.defaultdict(int)
        unique_fruits = 0
        total_fruits = 0
        start = 0
        end = 0
        for end in range(len(tree)):
            type_of_fruit = tree[end]
            fruit_basket[type_of_fruit] += 1
            if fruit_basket[type_of_fruit] == 1:
                unique_fruits += 1
            while unique_fruits > 2:
                start_fruit = tree[start]
                fruit_basket[start_fruit] -= 1
                if not fruit_basket[start_fruit]:
                    unique_fruits -= 1
                start += 1
            total_fruits = max(total_fruits, end - start + 1)
        return total_fruits
