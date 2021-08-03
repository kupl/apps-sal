class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        odd_jump = {}
        even_jump = {}
        index_ele = {index: ele for index, ele in enumerate(A)}
        # {0: 10. 2: 12, 1: 13}
        sorted_A = sorted(list(range(len(A))), key=lambda x: A[x])
        even_sorted_A = sorted(list(range(len(A))), key=lambda x: (A[x], -x))
        # cache = {}
        # sorted(index_ele.items(), key=lambda kv: (kv[1], kv[0]))
        # print(sorted_A)
        # [1: 3, 1:2, 2:0, 3:1, 4:4]
        # [4: 4, 3: 1, 2:0. 1:2, 1:3]
        # [4, 1, 0, 3]
        stack = []
        # [1, 1, 2,3,4]
        for i in range(len(A)):
            idx = sorted_A[i]
            # idx = ele_index[ele]
            while stack and stack[-1] < idx:
                old_index = stack.pop()
                odd_jump[old_index] = idx
            stack.append(idx)
        for idx in stack:
            odd_jump[idx] = -1
        stack = []
        for i in range(len(A) - 1, -1, -1):
            idx = even_sorted_A[i]
            # idx = ele_index[ele]
            while stack and stack[-1] < idx:
                old_index = stack.pop()
                even_jump[old_index] = idx
            stack.append(idx)
        for idx in stack:
            even_jump[idx] = -1
        self.ans = 0
        # print(odd_jump, even_jump)

        @lru_cache(None)
        def helper(index, odd):
            if index == len(A) - 1:
                # self.ans += 1
                return 1
            ans = 0
            if index == -1:
                return 0
            # if (index, odd) in self.cache: return self.cache[(index, odd)]
            if odd:
                # print(index)
                ans += helper(odd_jump[index], not odd)
            else:
                ans += helper(even_jump[index], not odd)
                # [10, 12, 13, 14, 15]
                # [0,   2,  1,  3,  4]
                # 1
                # 2   3   3  4 -1
                # [15, 14, 13, 12, 10]
                # [15, 14, 12, 10]
                #  -1        13: 2
            return ans
        ans = 0
        for i in range(len(A)):
            ans += helper(i, True)
        return ans
