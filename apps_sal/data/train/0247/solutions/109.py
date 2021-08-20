class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        (prefxSum, prefx) = (0, [])
        (suffxSum, suffx) = (sum(arr), [])
        dct = {0: -1}
        dp = [float('inf')] * len(arr)
        for i in range(0, len(arr)):
            x = arr[i]
            prefxSum += x
            prefx.append(prefxSum)
            suffx.append(suffxSum)
            suffxSum -= x
            dct[prefxSum] = i
        prefxSum = 0
        mn = float('inf')
        for i in range(0, len(arr)):
            prefxSum += arr[i]
            "\n                if prefxSum-arr[i] in dct:\n                    start=dct[prefxSum-arr[i]]\n                    if dp[start]!=float('inf'):\n                        mn=min(mn, dp[start]+dp[i])\n            "
            if prefxSum - target in dct:
                start = dct[prefxSum - target]
                if start > -1:
                    if dp[start] != float('inf'):
                        mn = min(mn, dp[start] + i - start)
                    dp[i] = min(dp[i - 1], i - start)
                else:
                    dp[i] = i + 1
            elif i > 0:
                dp[i] = dp[i - 1]
        return mn if mn != float('inf') else -1
        '\n        below brute force DOES NOT WORK\n        idx=[]\n        for i in range(0, len(arr)):\n            for j in range(i, len(arr)):\n                if sum(arr[i:(j+1)])==target:\n                    idx.append([j-i+1,i, j])\n        #print(idx)            \n        if len(idx)<2:\n            return -1\n        idx=sorted(idx)\n        #print(idx)\n        \n        a1=idx[0][0]\n        L0, i,j=idx[0]\n        for k in range(1, len(idx)):\n            L, start, end=idx[k]\n            #if not (start<=i<=end or start<=j<=end):\n            if not (i<=start<=j or i<=end<=j):\n                #idx.append([j-i+1,i, j])\n                a2=end-start+1\n                return a1+a2\n                \n        #return idx[0][0] + idx[1][0]\n        return -1\n        '
