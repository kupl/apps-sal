class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        if len(A) < 3:
            return 0

        count = 0
        l = len(A)

        i = 0
        while i < l - 2:
            j = i + 2
            while j < l:
                if A[i] - A[i + 1] == A[j - 1] - A[j]:
                    count += j - i - 1
                    j += 1
                else:
                    i = j - 1
                    break
            if j == l:
                break

        return count
