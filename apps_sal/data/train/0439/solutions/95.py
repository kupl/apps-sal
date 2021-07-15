class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        i, j = 0, 1
        res = 1
        while j < len(A) - 1:
            if A[i] == A[j] and i + 1 == j: # [100, 100, 100]
                # print('i:', i, 'A[i]:', A[i])
                # print('j:', j, 'A[j]:', A[j])
                i = j
                j += 1
            else:
                j += 1
                sign1, sign2 = 0, 0 # 0 for > and 1 for <
                if A[j] == A[j - 1] or A[j - 1] == A[j - 2]:
                    pass
                    # print('i:', i, 'A[i]:', A[i])
                    # print('j:', j, 'A[j]:', A[j])
                else:
                    if A[j] < A[j - 1]:
                        sign1 = 1
                    if A[j - 1] < A[j - 2]:
                        sign2 = 1
                if sign1 == sign2:
                    # print('i:', i, 'A[i]:', A[i])
                    # print('j:', j, 'A[j]:', A[j])
                    if j - i > res:
                        res = j - i
                    i = j - 1
        if j - i > res:
            # print('i:', i, 'A[i]:', A[i])
            # print('j:', j, 'A[j]:', A[j])
            res = j - i + 1
        return res
