class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) == 0 or len(tree) == 1:
            return len(tree)
        A = [-1] * 2
        B = [-1] * 2
        f1 = -1
        f2 = -1
        n = len(tree)
        maxi = 1
        i = 0
        while i < n:
            if tree[i] == f1 or tree[i] == f2:
                if tree[i] == f1:
                    A[1] = i
                else:
                    B[1] = i
            elif tree[i - 1] == f1:
                f2 = tree[i]
                A[0] = B[1] + 1
                B[0] = B[1] = i
            else:
                f1 = tree[i]
                B[0] = A[1] + 1
                A[0] = A[1] = i
            maxi = max(maxi, max(A[1], B[1]) - min(A[0], B[0]))
            i = i + 1
        return maxi + 1
