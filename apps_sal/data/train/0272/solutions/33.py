class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        N = len(status)
        scores = [0] * N
        for i in range(N):
            scores[i] += status[i]
        level = []
        for b in initialBoxes:
            scores[b] += N + 1
            if scores[b] >= N + 2:
                level.append(b)
                scores[b] = -sys.maxsize
        res = 0
        while level:
            n_level = []
            for b in level:
                res += candies[b]
                for k in containedBoxes[b]:
                    scores[k] += N + 1
                    if scores[k] >= N + 2:
                        n_level.append(k)
                        scores[k] = -sys.maxsize
                for k in keys[b]:
                    scores[k] += 1
                    if scores[k] >= N + 2:
                        n_level.append(k)
                        scores[k] = -sys.maxsize
            level = n_level
        return res
