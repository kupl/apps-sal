class Solution:

    def partitionDisjoint(self, A: List[int]) -> int:
        biggest = A[0]
        newbiggest = A[0]
        lenL = 1
        total = 1
        for itr in A[1:]:
            total += 1
            if itr < biggest:
                lenL = total
                biggest = newbiggest
            elif itr > newbiggest:
                newbiggest = itr
        return lenL
