class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        preSum = [0]
        for val in arr:
            preSum.append(preSum[-1] + val)
        sumMap = {}
        preCands = [sys.maxsize] * len(arr)
        sufCands = [sys.maxsize] * len(arr)
        for i, val in enumerate(preSum):
            if val - target in sumMap:
                sufCands[sumMap[val - target]] = i - sumMap[val - target]
                preCands[i - 1] = i - sumMap[val - target]
            sumMap[val] = i
        # print(preCands)
        # print(sufCands)
        
        prefixSum = [sys.maxsize] * len(arr)
        suffixSum = [sys.maxsize] * len(arr)
        for i, val in enumerate(preCands):
            if i + 1 < len(prefixSum):
                prefixSum[i + 1] = min(preCands[i],  prefixSum[i])
        for i, val in reversed(list(enumerate(sufCands))):
            if i + 1 < len(suffixSum):
                suffixSum[i] = min(sufCands[i], suffixSum[i + 1])
            else:
                suffixSum[i] = sufCands[i]
        # print(prefixSum)
        # print(suffixSum)
        
        res = sys.maxsize
        for i in range(len(arr)):
            res = min(res, prefixSum[i] + suffixSum[i])
            
        return res if res != sys.maxsize else -1
                
        
        
#         t = 6
        
# idx         0 1 2 3 4 5 6 7 8
        
# arr         1 2 3 3 2 1 1 1 1
#                 3 3
#             1 2 3
#                   3 2 1
#                      2 1 1 1 1
        
# preSum      0 1 3 6 9 11 12 13 14 15
        
# preCands    M M 3 2 M 3 M M 5
# sufCands    3 M 2 3 5 M M M M
        
# prefix      M M M 3 2 2 2 2 2
# suffix      2 2 2 3 5 M M M M
        

