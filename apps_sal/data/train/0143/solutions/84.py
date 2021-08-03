class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        total_len = len(tree)

        if total_len == 0:
            return 0

        rst = 1

        fruit_1 = tree[0]

        start = 0

        # Check the first fruit
        while tree[start] == fruit_1:
            start += 1
            if start >= total_len:
                return start

        # Check the second fruit
        fruits = [fruit_1, tree[start]]
        fruits_order = [start - 1, start]
        total_fruits = start + 1

        #print(fruits, fruits_order, total_fruits, start)

        for i in range(start + 1, total_len):
            # print(\"new_fruit is\", tree[i])
            if tree[i] == fruits[0]:
                fruits_order[0] = i
                total_fruits += 1
                # print(\"Update the basket 0\", fruits, fruits_order, total_fruits)

            elif tree[i] == fruits[1]:
                fruits_order[1] = i
                total_fruits += 1
                # print(\"Update the basket 1\", fruits, fruits_order, total_fruits)

            else:
                if total_fruits > rst:
                    rst = total_fruits
                if fruits_order[0] > fruits_order[1]:
                    fruits[1] = tree[i]
                    total_fruits = i - fruits_order[1]
                    fruits_order[1] = i
                else:
                    fruits[0] = tree[i]
                    total_fruits = i - fruits_order[0]
                    fruits_order[0] = i

                # print(\"generate the new fruits order, type\")
                #print(fruits, fruits_order, total_fruits)

        if total_fruits > rst:
            return total_fruits

        return rst
