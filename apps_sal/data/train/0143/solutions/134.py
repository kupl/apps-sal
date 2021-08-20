class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        k = 2
        start = 0
        freqHashmap = {}
        maxFruit = 0
        for end in range(len(tree)):
            freqHashmap[tree[end]] = freqHashmap.get(tree[end], 0) + 1
            while len(freqHashmap) > k:
                freqHashmap[tree[start]] -= 1
                if freqHashmap[tree[start]] == 0:
                    del freqHashmap[tree[start]]
                start += 1
            maxFruit = max(maxFruit, end - start + 1)
        return maxFruit
