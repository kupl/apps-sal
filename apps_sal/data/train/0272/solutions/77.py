class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        res, bcache, kcache = 0, set(initialBoxes), set()
        for _ in range(999):
            tmp = set()
            for b in bcache:
                if status[b] == 1 or b in kcache:
                    tmp |= set(containedBoxes[b])
                    kcache |= set(keys[b])
                    res += candies[b]
                else:
                    tmp.add(b)
            bcache = tmp
        # print(f'{bcache} {kcache}')
        return res
                    

