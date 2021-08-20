class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [float('-inf')] + A + [float('-inf')]
        stack = [0]
        res = 0
        for i in range(1, len(A)):
            while A[i] < A[stack[-1]]:
                j = stack.pop()
                k = stack[-1]
                res += A[j] * (i - j) * (j - k)
                res %= 10 ** 9 + 7
            stack.append(i)
        return res


'\n        if not A:\n            return 0\n        curmin = []\n        res = 0\n        for i in A:\n            curminlevel = []\n            if not curmin:\n                curminlevel.append(i)\n                res += i\n            else:\n                for j in range(len(curmin[-1])):\n                    minnum = min(curmin[-1][j], i)\n                    curminlevel.append(minnum)\n                    res += minnum\n                curminlevel.append(i)\n                res += i\n            curmin.append(curminlevel)\n        return res%(10**9 + 7)'
