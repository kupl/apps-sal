class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 1:
            return 1
        max_len = 1
        temp_len = 1
        odd_or_even = None
        last = A[0]
        for i in A[1:]:
            if i == last:
                odd_or_even = None
                temp_len = 1
                continue
            elif i > last:
                if odd_or_even == None or odd_or_even == 1:
                    odd_or_even = 0
                    temp_len += 1
                else:
                    odd_or_even = 0
                    temp_len = 2
            else:
                if odd_or_even == None or odd_or_even == 0:
                    odd_or_even = 1
                    temp_len += 1
                else:
                    odd_or_even = 1
                    temp_len = 2
            last = i
            max_len = max(max_len, temp_len)
        return max_len

