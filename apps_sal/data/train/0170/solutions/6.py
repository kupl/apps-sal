class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        answer = n - 1
        A = arr
        if len(arr) == 1:
            return 0
        flag = False
        for i in range(1, n):
            if A[i] < A[i - 1]:
                flag = True
                j = n - 1
                while (j > i and A[j] >= A[i - 1]) and (j == n - 1 or A[j] <= A[j + 1]):
                    j = j - 1
                answer = min(answer, j - i + 1)
                break
        if flag == False:
            return 0
        for i in range(n - 2, -1, -1):
            if A[i] > A[i + 1]:
                j = 0
                while (j < i and A[j] <= A[i + 1]) and (j == 0 or A[j] >= A[j - 1]):
                    j = j + 1
                answer = min(answer, i - j + 1)
                break
        return answer
