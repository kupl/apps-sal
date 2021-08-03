class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        def backtracking(idx):
            nonlocal memo, max_val
            if idx in memo:
                return memo[idx]
            lstack = []
            rstack = []
            lbarrier = False
            rbarrier = False
            for i in range(1, d + 1):
                if not lbarrier and idx - i >= 0 and arr[idx - i] < arr[idx]:
                    lstack.append(idx - i)
                else:
                    lbarrier = True
                if not rbarrier and idx + i < len(arr) and arr[idx + i] < arr[idx]:
                    rstack.append(idx + i)
                else:
                    rbarrier = True
            # if idx == 10: print(lstack, rstack)
            ljump = 1
            while lstack:
                lidx = lstack.pop()
                ljump = max(ljump, 1 + backtracking(lidx))
            rjump = 1
            while rstack:
                ridx = rstack.pop()
                rjump = max(rjump, 1 + backtracking(ridx))
            jump = max(ljump, rjump)
            memo[idx] = jump
            max_val = max(max_val, jump)
            return jump
        memo = {}
        max_val = 0
        for i in range(len(arr)):
            backtracking(i)

        return max_val
