import collections


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        left = 0
        right = 0
        fruitsTypes = defaultdict(int)
        numFruits = 0
        maxNumFruit = 0
        while(right < len(tree)):
            fruitsTypes[tree[right]] += 1
            numFruits += 1
            right += 1
            while len(fruitsTypes) > 2:
                fruitsTypes[tree[left]] -= 1
                if fruitsTypes[tree[left]] == 0:
                    del(fruitsTypes[tree[left]])
                numFruits -= 1
                left += 1
            maxNumFruit = max(maxNumFruit, numFruits)
        return maxNumFruit
