class Solution:

    def numTeams(self, rating: List[int]) -> int:
        combos = 0
        for (index, numba) in enumerate(rating[:-2]):
            for (indexy, numbay) in enumerate(rating[index + 1:-1]):
                for numbaz in rating[rating.index(numbay) + 1:]:
                    if numba < numbay and numbay < numbaz:
                        combos += 1
                    elif numba > numbay and numbay > numbaz:
                        combos += 1
        return combos
