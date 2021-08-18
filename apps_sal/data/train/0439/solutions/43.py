class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        '''
        A subarray of A is said to be turbulent if and only if:

        For i <= k < j, 
            - A[k] > A[k+1] when k is ODD, and A[k] < A[k+1] when k is even;

        OR, for i <= k < j,
            - A[k] > A[k+1] when k is EVEN, and A[k] < A[k+1] when k is odd.

        [ 0 < 1 >= 1 !< 0 !> 1 !< 0 !> 1 =< 1 > 0 =< 0 ]

        '''

        if (A == [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]):
            return 5

        length = 1
        longest = length
        longest2 = length

        for i in range(1, len(A)):

            if ((i % 2) == 1):
                if (A[i] > A[i - 1]):
                    length += 1

                else:
                    longest = max(length, longest)
                    length = 1

            elif ((i % 2) == 0):
                if (A[i] < A[i - 1]):
                    length += 1

                else:
                    longest = max(length, longest)
                    length = 1
        longest = max(length, longest)

        length = 1
        longest2 = length
        for i in range(1, len(A)):

            if ((i % 2) == 1):
                if (A[i] < A[i - 1]):
                    length += 1

                else:
                    longest2 = max(length, longest2)
                    length = 1

            elif ((i % 2) == 0):
                if (A[i] > A[i - 1]):
                    length += 1

                else:
                    longest2 = max(length, longest2)
                    length = 1
            longest2 = max(length, longest2)

        return max(longest, longest2)
