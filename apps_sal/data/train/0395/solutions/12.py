class Solution:

    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        smallestLarger = [-1] * n
        s = sorted(range(n), key=lambda i: A[i])
        stk = []
        for i in s:
            while stk and stk[-1] < i:
                smallestLarger[stk.pop()] = i
            stk.append(i)
        largestSmaller = [-1] * n
        s = sorted(range(n), key=lambda i: -A[i])
        stk = []
        for i in s:
            while stk and stk[-1] < i:
                largestSmaller[stk.pop()] = i
            stk.append(i)

        @lru_cache()
        def jump(i, odd):
            if i == n - 1:
                return True
            if i == -1:
                return False
            if odd:
                return jump(smallestLarger[i], 0)
            else:
                return jump(largestSmaller[i], 1)
        return sum((jump(i, 1) for i in range(n)))
