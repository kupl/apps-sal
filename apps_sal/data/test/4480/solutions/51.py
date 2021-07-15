class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0: return False
        return self.can_partition(A, 0, 3, s // 3) 
    
    def can_partition(self, A: List[int], i: int, n_parts: int, target_sum: int) -> bool:
        #print(f'i={i}, n_parts={n_parts}')
        if n_parts == 1: return i < len(A) and sum(A[i:]) == target_sum
        if i >= len(A): return False
        partition_sum = A[i]
        j = i + 1
        while j < len(A) and partition_sum != target_sum:
            partition_sum += A[j]
            j += 1
        return self.can_partition(A, j, n_parts - 1, target_sum)
