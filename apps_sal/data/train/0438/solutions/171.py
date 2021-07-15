class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
#         groups = [\"0\" for _ in range(len(arr))]
#         dp = defaultdict(lambda:0)
#         ctn = False
#         pdx = -1
        
#         for i in range(len(arr)): groups[arr[i]-1] = \"1\"
        
#         for i in range(len(groups)):
#             if groups[i] == \"0\":
#                 ctn = False
#             else:
#                 if not ctn:
#                     dp[i] += 1
#                     ctn = True; pdx = i
#                 else:
#                     dp[pdx] += 1
        
#         for key in dp:
#             if dp[key] == m: return len(arr)
#         keys = list(sorted(dp.keys()))
#         for i in range(len(arr))[::-1]:
#             idx = bisect.bisect_left(keys, arr[i]-1)
#             if ((0 < idx < len(keys) and keys[idx] != arr[i]-1)) or (idx == len(keys)): idx -= 1
#             key = keys[idx]
#             dif = arr[i]-1 - key
#             if dp[key]-dif-1 != 0:
#                 dp[arr[i]] = dp[key]-dif-1
#                 bisect.insort(keys, arr[i])
#                 if dp[arr[i]] == m: return i
#             dp[key] = dif
#             if dp[key] == m:
#                 return i
#             if dp[key] == 0: del dp[key]
    
#         return -1
        
        #双 list
        # length = [0] * (len(arr) + 2)
        # count = [0] * (len(arr) + 1)
        # res = -1
        # for i, a in enumerate(arr):
        #     left, right = length[a - 1], length[a + 1]
        #     length[a] = length[a - left] = length[a + right] = left + right + 1
        #     count[left] -= 1
        #     count[right] -= 1
        #     count[length[a]] += 1
        #     if count[m]:
        #         res = i + 1
        # return res
        
        #简单版 通过记录左右border
        if m==len(arr): return m
        
        border=[-1]*(len(arr)+2)
        ans=-1
        
        for i in range(len(arr)):
            left=right=arr[i]
            #left = arr[i]-1; right = arr[i]+1
            if border[right+1]>=0: right=border[right+1]
            if border[left-1]>=0: left=border[left-1]
            border[left], border[right] = right, left
            if (right-arr[i]==m) or (arr[i]-left==m):
                ans=i
        
        return ans
        
        
        
        
        
        
        
        
        
        

