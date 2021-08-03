class Solution:
    # def totalFruit(self, tree):
    #     # scan the array
    #     fruit_block = []
    #     #fruit_block entity = [left_most index in fruit, weight]
    #     for i in range(len(tree)):
    #         if i == 0 or tree[i] != tree[i-1]:
    #             fruit_block.append([i, 1 ])
    #         elif tree[i] == tree[i-1]:
    #             fruit_block[-1][1] += 1
    #     # print(fruit_block)
    #     max_fruit = 0
    #     i = 0
    #     while i < len(fruit_block):
    #         old_i = i
    #         type_fruit = []
    #         weight = 0
    #         for j in range(i, len(fruit_block)):
    #             if tree[fruit_block[j][0]] not in type_fruit:
    #                 type_fruit.append(tree[fruit_block[j][0]])
    #             weight += fruit_block[j][1]
    #             # print(\"type fruit \", type_fruit)
    #             # print(\"weight \", weight)
    #             if len(type_fruit) > 2:
    #                 # print(\"break\")
    #                 i = j -1
    #                 break
    #             max_fruit = max(max_fruit, weight)
    #             if j == len(fruit_block):
    #                 break
    #         if i == old_i:
    #             break
    #     return max_fruit

    #     def totalFruit(self, tree: List[int]) -> int:

    #         greattest_count = 0
    #         for i in range(len(tree)):
    #             if i > 0 and tree[i] == tree[i-1]:
    #                 print(i)
    #                 continue
    #             if i > 2 and tree[i] == tree[i-2] and tree[i-1] == tree[i-3] and tree[i] != tree[i-1] and self.checkRepeat(tree, i):
    #                 #add function to define tree[i-1] == the newest tree after ones that look like tree[i]
    #                 print(i)
    #                 continue
    #             fruit = self.pickFruit(i, tree)
    #             if fruit > greattest_count:
    #                 greattest_count = fruit
    #         return greattest_count

    #             # print(count)
    #             # print(greattest_count)

    #         return greattest_count

    #     def checkRepeat(self,tree, i):
    #         for j in range(i, len(tree)):
    #             if tree[j] != tree[i]:
    #                 return tree[j]==tree[i-1]
    #         return True

    #     def pickFruit(self, i, tree):
    #         count = 0
    #         basket=[\"\", \"\"]
    #         for j in range(i, len(tree)):
    #             if basket[0] == \"\":
    #                 basket[0] = tree[j]
    #                 # print(\"basket1: \", basket[0])
    #                 count += 1
    #                 # print(\"basket1\")
    #             elif tree[j] == basket[0]:
    #                 count+=1
    #                 # print(\"already in basket1\")
    #             elif basket[1] == \"\":
    #                 basket[1] = tree[j]
    #                 count += 1
    #                 # print(\"basket2: \", basket[1])
    #             elif tree[j] == basket[1]:
    #                 count += 1
    #                 # print(\"already in basket2\")
    #             elif tree[j] not in basket:
    #                 return count
    #             if j == len(tree)-1:
    #                 return count

    def totalFruit(self, tree: List[int]) -> int:
        basket1 = -1
        basket2 = -1
        max_fruit = 0
        start = 0
        end = 0
        i = 0
        while i < len(tree):
            if tree[i] == basket1 or tree[i] == basket2:
                if tree[i] != tree[i - 1]:
                    end = i
                i += 1
                continue
            if basket1 == -1:
                basket1 = tree[i]
                end = i
                i += 1
                continue
            if basket2 == -1:
                basket2 = tree[i]
                end = i
                i += 1
                continue
            print(i)
            print(end)
            weight = i - start
            max_fruit = max(max_fruit, weight)
            # max_fruit = 2 - 0 = 2
            i = end  # 1
            start = end  # 1
            basket1 = -1
            basket2 = -1
        # if start == 0:
        #     weight = len(tree)
        # else:
        #     weight = len(tree) - start - 1
        weight = len(tree) - start

        max_fruit = max(max_fruit, weight)

        return max_fruit
