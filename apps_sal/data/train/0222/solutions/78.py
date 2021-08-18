class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        exists = set(A)
        max_length = 2

        for i in range(len(A)):
            for j in range(i):
                first = A[i]
                second = A[j]

                start = second
                curr_length = 2

                while (first + second) in exists:
                    curr_length += 1
                    curr = first + second
                    second = first
                    first = curr
                max_length = max(max_length, curr_length)

        if max_length < 3:
            return 0
        return max_length

    def old_lenLongestFibSubseq(self, A: List[int]) -> int:
        exists = set(A)
        max_length = 2

        for i in range(len(A)):
            for j in range(i):
                b = A[i]
                a = A[j]
                curr_length = 2

                while (a + b) in exists:
                    curr_length += 1
                    curr = a + b
                    a = b
                    b = curr
                max_length = max(max_length, curr_length)

        if max_length <= 2:
            return 0
        return max_length
