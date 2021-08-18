class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:

        N = len(A)

        def makeNextArray(B):
            ans = [None] * N
            stack = []
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack[-1]] = i
                    stack.pop()
                stack.append(i)
            return ans

        increaseOrder = sorted(list(range(N)), key=lambda i: A[i])
        oddnext = makeNextArray(increaseOrder)
        decreaseOrder = sorted(list(range(N)), key=lambda i: -A[i])
        evennext = makeNextArray(decreaseOrder)

        odd = [False] * N
        even = [False] * N
        odd[N - 1] = True
        even[N - 1] = True
        for i in range(N - 2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]
        return sum(odd)
