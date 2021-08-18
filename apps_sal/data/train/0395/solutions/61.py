class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        if not A:
            return 0

        n = len(A)

        next_pos = [[-1] * 2 for _ in range(n)]

        stack = []

        idxes = sorted([i for i in range(n)], key=lambda i: (A[i], i))

        for idx in idxes:
            while stack and stack[-1] < idx:
                next_pos[stack[-1]][1] = idx
                stack.pop()

            stack.append(idx)

        stack = []

        idxes = sorted([i for i in range(n)], key=lambda i: (-A[i], i))

        for idx in idxes:
            while stack and stack[-1] < idx:
                next_pos[stack[-1]][0] = idx
                stack.pop()

            stack.append(idx)

        dp = [[False] * 2 for _ in range(n)]

        ret = 0

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                dp[i][0] = True
                dp[i][1] = True

            else:

                odd_next = next_pos[i][1]
                if odd_next == -1:
                    dp[i][1] = False
                else:
                    dp[i][1] = dp[odd_next][0]

                even_next = next_pos[i][0]
                if even_next == -1:
                    dp[i][0] = False
                else:
                    dp[i][0] = dp[even_next][1]

            if dp[i][1] == True:
                ret += 1

        return ret
