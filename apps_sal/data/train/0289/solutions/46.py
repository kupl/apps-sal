class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        l_subarray_sums = [sum(A[i:i + L]) for i in range(0, len(A) - L + 1)]
        m_subarray_sums = [sum(A[i:i + M]) for i in range(0, len(A) - M + 1)]
        max_sum = 0
        for (i, l_subarray_sum) in enumerate(l_subarray_sums):
            if not m_subarray_sums[i + L:]:
                continue
            max_complement = max(m_subarray_sums[i + L:])
            if l_subarray_sum + max_complement > max_sum:
                max_sum = l_subarray_sum + max_complement
                print(f'l sum : {l_subarray_sum} | m sum : {max_complement}')
        for (i, m_subarray_sum) in enumerate(m_subarray_sums):
            if not l_subarray_sums[i + M:]:
                continue
            max_complement = max(l_subarray_sums[i + M:])
            if m_subarray_sum + max_complement > max_sum:
                max_sum = m_subarray_sum + max_complement
                print(f'm sum : {m_subarray_sum} | m sum : {max_complement}')
        return max_sum
