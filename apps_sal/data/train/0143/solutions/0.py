class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        prior_fruit = tree[0]
        prior_fruit_counter = 0
        fruits_in_basket = [tree[0]]
        fruits_in_basket_counter = 0
        max_fib = -1
        for fruit in tree: 
            if prior_fruit == fruit:
                prior_fruit_counter += 1
                fruits_in_basket_counter += 1
            elif prior_fruit != fruit:
                if fruit in fruits_in_basket:
                    fruits_in_basket_counter += 1
                else:
                    fruits_in_basket, fruits_in_basket_counter = [prior_fruit, fruit], prior_fruit_counter + 1
                prior_fruit, prior_fruit_counter = fruit, 1
            if fruits_in_basket_counter > max_fib:
                max_fib = fruits_in_basket_counter
        return max_fib
