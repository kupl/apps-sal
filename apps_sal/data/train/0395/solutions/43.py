# Note: this is a difficult question
class Solution:
    # https://stackoverflow.com/questions/61242724/reaching-the-end-of-an-array-with-a-sequence-of-odd-even-jumps
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)

        def make(B):
            ans = [None] * N
            stack = []  # invariant: stack is decreasing
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(list(range(N)), key=lambda i: A[i])
        print(B)
        oddnext = make(B)
        print(oddnext)
        #B.sort(key = lambda i: -A[i])
        B = sorted(list(range(N)), key=lambda i: -A[i])
        print(B)
        evennext = make(B)
        print(evennext)

        odd = [False] * N
        even = [False] * N
        odd[N - 1] = even[N - 1] = True

        for i in range(N - 1, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        return sum(odd)
