class Solution:

    def int2arr(self, x, n):
        arr = []
        x1 = x
        for i in range(n):
            arr.append(x1 % 2)
            x1 = x1 // 2
        return arr

    def arr2int(self, arr):
        x = 0
        for i in range(len(arr)):
            x += arr[i] * 2 ** i
        return x

    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        overlap = {}
        for i in range(n):
            for j in range(n):
                short = min(len(A[i]), len(A[j]))
                for k in range(short, -1, -1):
                    if A[i][len(A[i]) - k:len(A[i])] == A[j][0:k]:
                        break
                overlap[i, j] = k
        state_order = []
        for i in range(0, n + 2):
            state_order.append([])
        for i in range(0, 2 ** n):
            arr = self.int2arr(i, n)
            state_order[sum(arr)].append(i)
        m = {}
        conn = {}
        for i in range(n):
            x = 2 ** i
            m[x, i] = len(A[i])
            conn[x, i] = A[i]
        for l in range(2, n + 1):
            for x in state_order[l]:
                arr = self.int2arr(x, n)
                for end in range(n):
                    if arr[end] == 1:
                        m[x, end] = 100000
                        x_prev = x - 2 ** end
                        arr_prev = self.int2arr(x_prev, n)
                        for prev in range(n):
                            if arr_prev[prev] == 1 and m[x_prev, prev] + len(A[end]) - overlap[prev, end] < m[x, end]:
                                m[x, end] = m[x_prev, prev] + len(A[end]) - overlap[prev, end]
                                conn[x, end] = conn[x_prev, prev] + A[end][overlap[prev, end]:len(A[end])]
        ans = 100000
        for i in range(n):
            if m[2 ** n - 1, i] < ans:
                ans = m[2 ** n - 1, i]
                ans_str = conn[2 ** n - 1, i]
        return ans_str
