class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        # biggest = A[0]
        # newbiggest = A[0]
        # lenL = 1
        # total = 1
        # for itr in A[1:]:
        #     total += 1
        #     if itr < biggest:
        #         lenL = total
        #         biggest = newbiggest
        #     else:
        #         if itr > newbiggest:
        #             newbiggest = itr
        # return lenL
        disjoint = 0
        v = A[disjoint]
        max_so_far = v
        for i in range(len(A)):
            max_so_far = max(max_so_far, A[i])
            if A[i] < v: 
                disjoint = i
                v = max_so_far
        return disjoint + 1
