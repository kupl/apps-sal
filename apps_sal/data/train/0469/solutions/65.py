class Solution:
    def validateBinaryTreeNodes(self, n, left, right):
        roots = {*range(n)}
        for x in left + right:
            if x == -1:
                continue
            if x not in roots:
                return False
            roots.discard(x)
        if len(roots) != 1:
            return False
        root = roots.pop()
        stk = [root]
        k = 0
        while stk:
            node = stk.pop()
            k += 1
            l, r = left[node], right[node]
            if l != -1:
                stk.append(l)
            if r != -1:
                stk.append(r)
        return k == n
