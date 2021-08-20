class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        xorarr = [arr[0]]
        for i in range(1, n):
            xorarr.append(xorarr[-1] ^ arr[i])
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if xorarr[k] ^ xorarr[j - 1] == xorarr[j - 1] ^ (xorarr[i - 1] if i > 0 else 0):
                        count += 1
        return count
