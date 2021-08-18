class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        rec = set()
        log = {}

        def check(ind, tar):
            if ind == -1:
                return False
            if ind in log:
                if log[ind] == tar:
                    return True
                return check(log[ind], tar)
            return False
        for ind, (i, j) in enumerate(zip(leftChild, rightChild)):
            if i != -1:
                if i in rec:
                    return False
                rec.add(i)
                log[i] = ind
                if check(ind, i):
                    return False
            if j != -1:
                if j in rec:
                    return False
                rec.add(j)
                log[j] = ind
                if check(ind, j):
                    return False
        if len(rec) + 1 != n:
            return False
        return True
