class Solution:

    def maxJumps(self, A: List[int], d: int) -> int:
        """
        6 4
        14 -> 6, (0), 14 -> 4 (1)
        14 -> (3), 
        14 -> (4), (4) -> (3)

        """
        n = len(A)
        graph = {}
        inorder = [0] * n
        for i in range(n):
            graph[i] = []
            is_greater = False
            cur_max = -1
            for ind in range(i - 1, max(-1, i - d - 1), -1):
                if A[ind] >= A[i]:
                    if A[ind] >= cur_max and A[ind] > A[i]:
                        cur_max = A[ind]
                        graph[ind].append(i)
                        inorder[i] += 1
                    is_greater = True
                else:
                    if is_greater:
                        continue
                    graph[i].append(ind)
                    inorder[ind] += 1
        stack = []
        dp = [1] * n
        for i in range(n):
            if inorder[i] == 0:
                stack.append(i)
        while stack:
            top = stack.pop()
            for value in graph[top]:
                inorder[value] -= 1
                dp[value] = max(dp[value], dp[top] + 1)
                if inorder[value] == 0:
                    stack.append(value)
        return max(dp)
