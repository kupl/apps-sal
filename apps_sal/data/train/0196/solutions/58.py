class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:

        n = len(A)
        max_sub_ending = [A[0]]
        max_sub_ending_index = [0]

        for i in range(1, len(A)):
            prev = max_sub_ending[i - 1]
            if prev <= 0:
                max_sub_ending_index.append(i)
                max_sub_ending.append(A[i])
            else:
                max_sub_ending_index.append(max_sub_ending_index[-1])
                max_sub_ending.append(A[i] + max_sub_ending[-1])
        print(max_sub_ending)
        posmax = max(max_sub_ending)
        total = sum(A)

        for i in range(len(A)):
            A[i] = -A[i]
        max_sub_ending = [A[0]]
        max_sub_ending_index = [0]

        for i in range(1, len(A)):
            prev = max_sub_ending[i - 1]
            if prev <= 0:
                max_sub_ending_index.append(i)
                max_sub_ending.append(A[i])
            else:
                max_sub_ending_index.append(max_sub_ending_index[-1])
                max_sub_ending.append(A[i] + max_sub_ending[-1])
        print(max_sub_ending)
        negmax = max(max_sub_ending) + total
        if negmax > posmax and negmax != 0:
            return negmax
        else:
            return posmax
