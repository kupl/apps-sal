class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        def find_maxsum(arr, l, m):
            max_sum = 0
            for i in range(len(arr) - l):
                l_slice = arr[i:i + l]
                l_sum = sum(l_slice)
                for j in range(i + l, len(arr) - m + 1):
                    m_slice = arr[j:j + m]
                    m_sum = sum(m_slice)
                    max_sum = max(max_sum, l_sum + m_sum)
            return max_sum

        def maximum_sum(arr, l, m):
            rev_arr = list(reversed(arr))
            return max(find_maxsum(arr, l, m), find_maxsum(rev_arr, l, m))
        return maximum_sum(A, L, M)
