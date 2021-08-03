from functools import lru_cache


class Solution:
    def shortestCommonSupersequence(self, a, b):
        mem = {}
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    mem[(i, j)] = 1 + (mem[(i - 1, j - 1)] if i - 1 >= 0 and j - 1 >= 0 else i + j)
                else:
                    mem[(i, j)] = 1 + min(mem[(i - 1, j)] if i - 1 >= 0 else j + 1, mem[(i, j - 1)] if j - 1 >= 0 else i + 1)

        stack = []
        i, j = (len(a) - 1, len(b) - 1)
        while(not(i == -1 or j == -1)):
            if a[i] == b[j]:
                stack.append(a[i])
                i, j = i - 1, j - 1
            else:
                if (mem[(i - 1, j)] if i - 1 >= 0 else j + 1) <= (mem[(i, j - 1)] if j - 1 >= 0 else i + 1):
                    stack.append(a[i])
                    i -= 1
                else:
                    stack.append(b[j])
                    j -= 1
        if j >= 0:
            stack.append(b[:j + 1])
        if i >= 0:
            stack.append(a[:i + 1])
        return ''.join(stack[::-1])
