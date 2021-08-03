class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 1:
            return 1

        sign = -(A[1] - A[0])
        max_length = 1
        cur_length = 1
        for i in range(1, len(A)):
            # print(A[i - 1], A[i], \" -- \", cur_length, sign)

            if A[i - 1] < A[i] and sign < 0:
                cur_length += 1
            elif A[i - 1] > A[i] and sign > 0:
                cur_length += 1
            else:
                max_length = max(max_length, cur_length)
                if A[i - 1] != A[i]:
                    cur_length = 2
                else:
                    cur_length = 1

            sign = A[i] - A[i - 1]

        max_length = max(max_length, cur_length)

        return max_length
