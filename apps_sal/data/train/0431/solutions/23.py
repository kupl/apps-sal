class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        stack = []
        l_count = []
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            l_c = 0
            if stack:
                l_c = stack[-1] + 1
            stack.append(i)
            l_count.append(l_c)

        stack = []
        r_count = []
        for i in range(n):
            while stack and A[stack[-1]] >= A[n - i - 1]:
                stack.pop()
            r_c = n - 1
            if stack:
                r_c = stack[-1] - 1
            stack.append(n - i - 1)
            r_count.append(r_c)

        r_count = r_count[::-1]

        t = 0
        print(l_count)
        print(r_count)
        for i in range(n):
            l = l_count[i]
            r = r_count[i]
            t += (i - l + 1) * (r - i + 1) * A[i]

        return t % (10**9 + 7)
