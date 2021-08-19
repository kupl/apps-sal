class Solution:

    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)

        def makeorder(sortedIdx):
            ans = [-1] * N
            stack = []
            for i in sortedIdx:
                while stack and i > stack[-1]:
                    ans[stack[-1]] = i
                    stack.pop()
                stack.append(i)
            return ans
        sortedIdx = sorted(range(N), key=lambda i: A[i])
        oddNext = makeorder(sortedIdx)
        sortedIdx = sorted(range(N), key=lambda i: -A[i])
        evenNext = makeorder(sortedIdx)
        odd = [False] * N
        even = [False] * N
        odd[N - 1] = True
        even[N - 1] = True
        for i in range(N - 2, -1, -1):
            if oddNext[i] != -1:
                odd[i] = even[oddNext[i]]
            if evenNext[i] != -1:
                even[i] = odd[evenNext[i]]
        return sum(odd)
