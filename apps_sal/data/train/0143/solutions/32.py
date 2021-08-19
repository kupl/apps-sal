class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # need to identify longest streak of two unique types of fruit

        # brute force
        #
        # loop i
        #
        #   loop j
        #       if dict < 2 then add unique character to dict
        #       if num encountered is not in dict and dict.len == 2 then break
        #  check if the counter > max if it is then set max to counter

        #         answer = 0
        #         counter = 0
        #         dictionary = {}
        #         # print(tree)
        #         for i in range(len(tree)):
        #             for j in range(i, len(tree)):
        #                 # print('curr', tree[j], i, j)
        #                 if tree[j] in dictionary:
        #                     counter += 1
        #                 elif tree[j] not in dictionary and len(dictionary) < 2:
        #                     counter += 1
        #                     dictionary[tree[j]] = tree[j]
        #                 elif tree[j] not in dictionary and len(dictionary) == 2:
        #                     break
        #             # print('round done')
        #             if counter > answer:
        #                 answer = counter
        #                 # print('reassigning answer', answer)
        #             counter = 0
        #             dictionary = {}

        #         return answer

        # something faster

        answer = 0
        currTree = 0
        numsDictionary = collections.Counter()

        for treeIndex, fruit in enumerate(tree):
            numsDictionary[fruit] += 1
            while len(numsDictionary) >= 3:
                numsDictionary[tree[currTree]] -= 1
                if numsDictionary[tree[currTree]] == 0:
                    del numsDictionary[tree[currTree]]
                currTree += 1
            answer = max(answer, treeIndex - currTree + 1)
        return answer
