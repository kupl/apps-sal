class Solution:

    def numTeams(self, rating: List[int]) -> int:
        l = len(rating)
        res = 0
        for (i, vi) in enumerate(rating):
            if i >= l - 2:
                break
            for (j, vj) in enumerate(rating[i + 1:]):
                if j >= l - 1:
                    break
                for (k, vk) in enumerate(rating[i + j + 1:]):
                    if vi < vj and vj < vk or (vi > vj and vj > vk):
                        res += 1
        return res
