class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        def right_boundry(A, dupl):
            res = [0] * len(A)
            A.append(-math.inf)
            stack = []

            for i in range(len(A)):
                if dupl:
                    while stack and A[stack[-1]] > A[i]:
                        j = stack.pop()
                        res[j] = i - j
                else:
                    while stack and A[stack[-1]] >= A[i]:
                        j = stack.pop()
                        res[j] = i - j

                stack.append(i)

            A.pop()
            return res

        right = right_boundry(A, False)
        left = right_boundry(A[::-1], True)[::-1]

        ans = sum([right[i] * left[i] * A[i] for i in range(len(A))])

        return ans % (10**9 + 7)
