class Solution:

    def minOperationsMaxProfit(self, arr: List[int], bc: int, rc: int) -> int:
        l = len(arr)
        groups = []
        rem = 0
        for i in range(l):
            avail = arr[i] + rem
            if avail >= 4:
                avail -= 4
                groups.append(4)
                rem = avail
            else:
                rem = 0
                groups.append(avail)
        while rem > 0:
            if rem >= 4:
                rem -= 4
                groups.append(4)
            else:
                groups.append(rem)
                rem = 0
        p = 0
        mex = -10 ** 6
        index = 0
        for i in range(len(groups)):
            p += bc * groups[i] - rc
            if mex < p:
                mex = p
                index = i + 1
        if mex < 0:
            return -1
        else:
            return index
