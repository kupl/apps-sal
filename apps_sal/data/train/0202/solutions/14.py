class Solution:
    def longestMountain(self, A: List[int]) -> int:

        i = 0
        answer = 0
        while i < len(A) - 1:

            j = i + 1
            visited_top = False

            while j < len(A):
                print(i, j)
                if A[j] > A[j - 1]:
                    if visited_top:
                        break

                if A[j] < A[j - 1]:
                    if not visited_top:
                        if j - i == 1:
                            break
                        visited_top = True

                if A[j] == A[j - 1]:
                    break
                j += 1

            if visited_top and j - i > 2:
                answer = max(answer, j - i)
            i = j
            if visited_top:
                i -= 1

        return answer
