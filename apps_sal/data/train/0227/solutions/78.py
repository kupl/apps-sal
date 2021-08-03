class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeros, ones, max_len = 0, 0, 0

        def element_found(element, inc):
            nonlocal zeros, ones, max_len
            if element == 0:
                zeros += inc
            else:
                ones += inc

        start = 0
        for element in A:
            element_found(element, 1)

            while zeros > K:
                start, start_element = start + 1, A[start]
                element_found(start_element, -1)

            max_len = max(max_len, zeros + ones)
        return max_len
