class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        # Monotonic Stack
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        # N = len(A)

        # def make(B):
        #     ans = [None] * N
        #     stack = []  # invariant: stack is decreasing
        #     for i in B:
        #         while stack and i > stack[-1]:
        #             ans[stack.pop()] = i
        #         stack.append(i)
        #     return ans

        # B = sorted(range(N), key=lambda i: A[i])
        # oddnext = make(B)
        # B.sort(key=lambda i: -A[i])
        # evennext = make(B)

        # odd = [False] * N
        # even = [False] * N
        # odd[N - 1] = even[N - 1] = True

        # for i in range(N - 2, -1, -1):
        #     if oddnext[i] is not None:
        #         odd[i] = even[oddnext[i]]
        #     if evennext[i] is not None:
        #         even[i] = odd[evennext[i]]

        # return sum(odd)


        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1

        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]

        return sum(higher)

