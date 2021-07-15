class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for id_i, i in enumerate(rating):
            for id_j, j in enumerate(rating[id_i:]):
                id_ij = id_i + id_j
                for id_k, k in enumerate(rating[id_ij:]):
                    id_ijk = id_ij + id_k
                    if 0<=i and id_i < id_ij and id_ij < id_ijk:
                        if i < j and j < k:
                            count += 1
                        if i > j and j > k:
                            count += 1
        return count
