class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        sumArr = []
        sumMap = {}
        sumMap[0] = -1
        
        for i in range(len(arr)):
            sumArr.append(arr[i] + (sumArr[i-1] if i-1 > -1 else 0))
            sumMap[sumArr[i]] = i
            
        #print(sumArr)
        #print(sumMap)
        
        res = math.inf
        
        dp = [math.inf for i in range(len(arr))]
        
        for i in range(0, len(arr)):
            if sumMap.get(sumArr[i] - target) != None:
                dp[i] = min(i - sumMap[sumArr[i] - target], dp[i-1] if i>0 else math.inf)
            else:
                dp[i] = dp[i-1] if i>0 else math.inf
                
        print(dp)
        
        for i in range(len(arr)-1, -1, -1):
            #print(\"arr:%d\"%(sumArr[i]))
            #print(sumMap.get(sumArr[i] - target))
            if sumMap.get(sumArr[i] - target) != None:
                j = sumMap.get(sumArr[i] - target)
                print(j)
                l1 = i - j
                if j > -1 and dp[j] != math.inf:
                    res = min(res, l1 + dp[j])
                
                
        return -1 if res == math.inf else res
