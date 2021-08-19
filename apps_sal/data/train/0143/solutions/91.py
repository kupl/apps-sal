class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        left_pointer, right_pointer = 0, 0
        fruits = 0
        fruits_in_basket = {}

        while (right_pointer < len(tree)):
            if (len(fruits_in_basket) <= 2):
                fruits_in_basket[tree[right_pointer]] = right_pointer
                right_pointer += 1
                # print(fruits_in_basket)
            if (len(fruits_in_basket) > 2):
                minimum_index = len(tree)
                for index in list(fruits_in_basket.values()):
                    minimum_index = min(minimum_index, index)
                left_pointer = minimum_index + 1
                # print(left_pointer)
                fruits_in_basket.pop(tree[minimum_index])
            fruits = max(fruits, (right_pointer - left_pointer))
            # print(fruits)

        return fruits
