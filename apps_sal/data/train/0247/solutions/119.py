class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        presum = [0] * len(arr)
        c = 0
        for i in range(len(arr)):
            c += arr[i]
            presum[i] = c
        dic = {0: -1}
        index = [0] * len(arr)
        short = [0] * len(arr)
        temp = sys.maxsize
        for i in range(len(arr)):
            if presum[i] - target in dic:
                index[i] = (i - dic[presum[i] - target])
                temp = min(temp, i - dic[presum[i] - target])
            dic[presum[i]] = i
            short[i] = temp

        ans = sys.maxsize
        print((index, short))
        for i in range(1, len(arr)):

            if index[i] > 0 and i - index[i] >= 0 and (short[i - index[i]] != sys.maxsize):

                ans = min(ans, short[i - index[i]] + index[i])

        if ans == sys.maxsize:
            return -1
        return ans

        # [3,1,1,1,5,1,2,1]
        # 3 4 5 6 11 12 14 15

       # 1 0 0 3 0 0.  2. 2
