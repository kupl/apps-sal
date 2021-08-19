class Solution:
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
        oddnext = make(B)
        print((oddnext, B))
        B.sort(key=lambda i: -A[i])
        evennext = make(B)

        dest = len(A) - 1
        cnt = 0
        for idx in range(N):
            jump, ptr = 1, idx
            while ptr != None:
                if ptr == dest:
                    cnt += 1
                    break
                jump, ptr = (0, oddnext[ptr]) if jump == 1 else (1, evennext[ptr])
        return cnt
