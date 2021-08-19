class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        cl = []
        stack = []
        for i in range(len(A)):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            if not stack:
                l = i + 1
            else:
                l = i - stack[-1]
            cl.append(l)
            stack.append(i)
        cr = []
        stack = []
        for i in range(len(A) - 1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            if not stack:
                r = len(A) - i
            else:
                r = stack[-1] - i
            stack.append(i)
            cr.append(r)
        cr = cr[::-1]
        tot = 0
        for i in range(len(A)):
            tot += A[i] * cl[i] * cr[i]
            tot %= 10 ** 9 + 7
        return tot
        '\n        queue = deque()\n        MOD = 10**9 + 7\n        \n        tot = 0\n        for indx, num in enumerate(A):\n            tot += num\n            queue.append((num,indx+1))\n            \n        while queue:\n            sub_min, indx = queue.popleft()\n            if indx < len(A):\n                new_sub_min = min(sub_min, A[indx])\n                queue.append((new_sub_min, indx+1))\n                tot += new_sub_min\n                tot %= MOD\n        \n        return tot\n        '
