class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        counter = {}
        start = 0
        maxL = 0
        for end in range(len(tree)):
            if tree[end] in counter:
                counter[tree[end]] += 1
            else:
                counter[tree[end]] = 1
            while len(counter) > 2:
                counter[tree[start]] -= 1
                if counter[tree[start]] == 0:
                    del counter[tree[start]]
                start += 1
            maxL = max(maxL, end - start + 1)
        return maxL
