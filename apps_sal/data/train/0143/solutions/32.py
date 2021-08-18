class Solution:
    def totalFruit(self, tree: List[int]) -> int:

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
