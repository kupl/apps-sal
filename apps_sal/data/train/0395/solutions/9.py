class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)

        def make(B):
            ans = [None] * N
            stack = []
            for v in B:
                while stack and v > stack[-1]:
                    ans[stack.pop()] = v
                stack.append(v)

            return ans

        B = sorted(range(N), key=lambda i: A[i])

        oddnext = make(B)

        B.sort(key=lambda i: -A[i])

        evennext = make(B)

        odd = [False] * N
        even = [False] * N

        odd[N - 1] = even[N - 1] = True

        for i in range(N - 2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        return sum(odd)
