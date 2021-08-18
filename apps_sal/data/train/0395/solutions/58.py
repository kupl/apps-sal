class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        odd_jump = {}
        even_jump = {}
        index_ele = {index: ele for index, ele in enumerate(A)}
        sorted_A = sorted(list(range(len(A))), key=lambda x: A[x])
        even_sorted_A = sorted(list(range(len(A))), key=lambda x: (A[x], -x))
        stack = []
        for i in range(len(A)):
            idx = sorted_A[i]
            while stack and stack[-1] < idx:
                old_index = stack.pop()
                odd_jump[old_index] = idx
            stack.append(idx)
        for idx in stack:
            odd_jump[idx] = -1
        stack = []
        for i in range(len(A) - 1, -1, -1):
            idx = even_sorted_A[i]
            while stack and stack[-1] < idx:
                old_index = stack.pop()
                even_jump[old_index] = idx
            stack.append(idx)
        for idx in stack:
            even_jump[idx] = -1
        self.ans = 0

        @lru_cache(None)
        def helper(index, odd):
            if index == len(A) - 1:
                return 1
            ans = 0
            if index == -1:
                return 0
            if odd:
                ans += helper(odd_jump[index], not odd)
            else:
                ans += helper(even_jump[index], not odd)
            return ans
        ans = 0
        for i in range(len(A)):
            ans += helper(i, True)
        return ans
