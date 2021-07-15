from functools import reduce
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        # (small value, small index) => (large value, large index)
        sorted_A = [i for _,i in sorted([(A[i],i) for i in range(len(A))])]
        memo = [[None for i in range(len(A))] for j in range(2)]
        
        def is_good_index(i):
            nonlocal sorted_A
            nonlocal A
            nonlocal memo
            
            def is_good(i, is_odd):
                nonlocal sorted_A
                nonlocal A
                nonlocal memo

                if sorted_A[i] == len(A)-1:
                    return True

                if memo[is_odd][i] is None:
                    memo[is_odd][i] = False
                    if is_odd:
                        for j in range(i+1, len(A)):
                            if sorted_A[i] < sorted_A[j]:
                                memo[is_odd][i] = is_good(j, not is_odd)
                                break
                    elif i+1 < len(A) and A[sorted_A[i+1]] == A[sorted_A[i]]:
                        memo[is_odd][i] = is_good(i+1, not is_odd)
                    else:
                        for j in range(i-1, -1, -1):
                            if sorted_A[i] < sorted_A[j]:
                                if j-1 >= 0 and sorted_A[i] < sorted_A[j-1] and A[sorted_A[j]] == A[sorted_A[j-1]]:
                                    continue
                                memo[is_odd][i] = is_good(j, not is_odd)
                                break

                return memo[is_odd][i]
            
            return is_good(i, True)
        
        return reduce(lambda x,y: x+is_good_index(y),list(range(len(A))),0)

