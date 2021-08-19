class Solution:

    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        dic = {}
        for i in range(len(A)):
            for j in range(len(A[i])):
                pos = A[i][j]
                if pos != 1:
                    continue
                for x in range(len(B)):
                    for y in range(len(B[x])):
                        pos = B[x][y]
                        if pos != 1:
                            continue
                        (xdiff, ydiff) = (y - j, x - i)
                        if (xdiff, ydiff) not in dic:
                            dic[xdiff, ydiff] = 1
                        else:
                            dic[xdiff, ydiff] += 1
        if len(dic) == 0:
            return 0
        return max(dic.values())
