class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        def findNextHighestIdx(B: List[int]) -> List[int]:
            next_idx_list = [None] * len(B)
            stack = []
            for i in B:
                while stack and stack[-1] < i:
                    next_idx_list[stack.pop()] = i
                stack.append(i)
            return next_idx_list

        N = len(A)
        B = sorted(range(N), key=lambda i: A[i])
        oddnextidx = findNextHighestIdx(B)
        B.sort(key=lambda i: -A[i])
        evennextidx = findNextHighestIdx(B)

        odd = [False] * N
        odd[N - 1] = True
        even = [False] * N
        even[N - 1] = True

        for i in range(N - 2, -1, -1):
            if oddnextidx[i] is not None:
                odd[i] = even[oddnextidx[i]]
            if evennextidx[i] is not None:
                even[i] = odd[evennextidx[i]]

        return sum(odd)
