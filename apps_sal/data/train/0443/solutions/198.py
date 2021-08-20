class Solution:

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        def get_triplets(r):
            res = 0
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        res += 1 if r[i] < r[j] < r[k] else 0
            return res
        return get_triplets(rating) + get_triplets(rating[::-1])
