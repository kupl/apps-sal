from itertools import cycle, islice
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        # solution 1
        count = 0
        for id_i, i in enumerate(rating):
            for id_j, j in enumerate(rating[id_i:]):
                id_ij = id_i + id_j
                for id_k, k in enumerate(rating[id_ij:]):
                    id_ijk = id_ij + id_k
                    if 0<=i:
                        if i < j and j < k:
                            count += 1
                        if i > j and j > k:
                            count += 1
        return count
    
    
        # solution 2 - itertools-islice
        # count = 0
        # print(list(islice(rating, 0)))
        # return count
    
        # solution 3 - numpy
        # count = 0
        # arr = rating
        # for i in range(arr.shape[0]):
        #     ij = i+j
        #     for j in range(arr[i:]):
        #         for k in range(arr[ij:]):
        #             ijk = ij + k
        #             if arr[i] > 0
            
        #return count

