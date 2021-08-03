class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefxSum, prefx = 0, []
        suffxSum, suffx = sum(arr), []
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
            # if prefxSum==target:
            #    dp[i]=1
            '''
                if prefxSum-arr[i] in dct:
                    start=dct[prefxSum-arr[i]]
                    if dp[start]!=float('inf'):
                        mn=min(mn, dp[start]+dp[i])
            '''
            if prefxSum - target in dct:
                start = dct[prefxSum - target]
                # print(\"i: \",i,\", j: \",dct[prefxSum-target])
                if start > -1:
                    if dp[start] != float('inf'):
                        mn = min(mn, dp[start] + i - start)
                    dp[i] = min(dp[i - 1], i - start)
                else:
                    dp[i] = i + 1
            elif i > 0:
                dp[i] = dp[i - 1]
        # print(dp)
        return mn if mn != float('inf') else -1
        '''
        below brute force DOES NOT WORK
        idx=[]
        for i in range(0, len(arr)):
            for j in range(i, len(arr)):
                if sum(arr[i:(j+1)])==target:
                    idx.append([j-i+1,i, j])
        #print(idx)            
        if len(idx)<2:
            return -1
        idx=sorted(idx)
        #print(idx)
        
        a1=idx[0][0]
        L0, i,j=idx[0]
        for k in range(1, len(idx)):
            L, start, end=idx[k]
            #if not (start<=i<=end or start<=j<=end):
            if not (i<=start<=j or i<=end<=j):
                #idx.append([j-i+1,i, j])
                a2=end-start+1
                return a1+a2
                
        #return idx[0][0] + idx[1][0]
        return -1
        '''
