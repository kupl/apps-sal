class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        max_l = 0
        list_poss = [{} for i in range(len(A))]
        for i in range(len(A) - 1):
            for j in range(i+1):
                if not (A[i+1] + A[j]) in list_poss[i+1]:
                    list_poss[i+1][A[i+1] + A[j]] = 2
                if A[i+1] in list_poss[j]:
                    if not(A[i+1] + A[j]) in list_poss[i+1]:
                        list_poss[i+1][A[i+1] + A[j]] = list_poss[j][A[i+1]] + 1
                    else:
                        if list_poss[j][A[i+1]] + 1 > list_poss[i+1][A[i+1] + A[j]]: 
                            list_poss[i+1][A[i+1] + A[j]] = list_poss[j][A[i+1]] + 1
                    if list_poss[i+1][A[i+1] + A[j]] > max_l:
                        max_l = list_poss[i+1][A[i+1] + A[j]]
                        
#            print(list_poss[i+1])
                        
        return max_l
