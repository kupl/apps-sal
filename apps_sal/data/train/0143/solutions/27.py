class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        #tree = [0,1,6,6,4,4,6]
        max_fruits = 0
        counter = 0
        fruit_basket = set()
        i = 0
        while i < len(tree):
            if len(fruit_basket) < 2 :
                counter += 1
                fruit_basket.add(tree[i])
                if len(fruit_basket) == 2:
                    new_fruit_idx = i
            elif tree[i] in fruit_basket:
                counter += 1
            else:
                fruit_basket = set()
                max_fruits = max(counter,max_fruits)
                counter = 0
                i = new_fruit_idx - 1
            i += 1
        max_fruits = max(counter,max_fruits)
        return max_fruits
