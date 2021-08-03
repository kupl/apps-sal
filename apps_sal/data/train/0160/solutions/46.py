def memoize(f):
    memo = {}

    def inner(*args):
        tup = tuple(args)
        if tup in memo:
            return memo[tup]
        res = f(*args)
        memo[tup] = res
        return res
    return inner


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def score(i=0, j=len(piles) - 1):
            if i == j:
                return piles[i]
            if (i, j) in memo:
                return memo[(i, j)]
            lscore = piles[j] - score(i, j - 1)
            rscore = piles[i] - score(i + 1, j)
            result = max(lscore, rscore)
            memo[(i, j)] = result
            return result
        return score() > 0
