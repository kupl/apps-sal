def find(dp,start,end,k,arr):
    if start > end:
        return -float('inf')
    if k <= 0:
        return -float('inf')
    if (start,end,k) in dp.keys():
        return dp[(start,end,k)]

    if start == end:
        if k == 1:
            return arr[start]
        return 0
    
    ans = 0
    total = 0
    count = 0
    for i in range(start,end+1):
        total += arr[i]
        count += 1
        if k-1 > 0:
            find(dp,i+1,end,k-1,arr)
            ans = max(ans,(total/count)+find(dp,i+1,end,k-1,arr))

    ans = max(ans,total/count)
    dp[(start,end,k)] = ans

    return ans

class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        dp = {}
        return find(dp,0,len(A)-1,K,A)
