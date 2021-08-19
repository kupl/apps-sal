class Solution:

    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        s1 = []
        s2 = []
        stack = []
        e = enumerate(A)
        order = sorted(e, key=lambda x: (x[1], x[0]))
        for i in reversed(list(range(n))):
            while stack and stack[-1] < order[i][0]:
                stack.pop()
            order[i] = (order[i][0], stack[-1]) if stack else (order[i][0], -1)
            stack.append(order[i][0])
        arr_odd = [-1] * n
        for i in range(n):
            arr_odd[order[i][0]] = order[i][1]
        stack = []
        e = enumerate(A)
        order = sorted(e, key=lambda x: x[1], reverse=True)
        for i in reversed(list(range(n))):
            while stack and stack[-1] < order[i][0]:
                stack.pop()
            order[i] = (order[i][0], stack[-1]) if stack else (order[i][0], -1)
            stack.append(order[i][0])
        arr_even = [-1] * n
        for i in range(n):
            arr_even[order[i][0]] = order[i][1]
        DP = [[False] * 2 for _ in range(n)]
        DP[n - 1][0] = True
        DP[n - 1][1] = True
        for i in reversed(list(range(n - 1))):
            if arr_odd[i] == n - 1:
                DP[i][0] = True
            elif arr_odd[i] != -1:
                DP[i][0] = DP[arr_odd[i]][1]
            if arr_even[i] == n - 1:
                DP[i][1] = True
            elif arr_even[i] != -1:
                DP[i][1] = DP[arr_even[i]][0]
        count = 0
        for i in range(n):
            if DP[i][0] == True:
                count += 1
        return count
