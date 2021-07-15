n = int(input())
num_list = list(map(int, input().split()))
# def lower_bound(min_lis, x): 
#     #goal return the position of the first element >= x
#     left = 0 
#     right = len(min_lis) - 1
#     res = -1
#     while left <= right:
#         mid = (left + right) // 2 
#         if min_lis[mid] < x: 
#             left = mid + 1
#         else:
#             res = mid
#             right = mid - 1
#     return res
import bisect

def LongestIncreasingSubsequence(a, n):
    min_lis = []
    #lis = [0 for i in range(n)]
    for i in range(n): 
        pos = bisect.bisect_left(min_lis, a[i])
        if pos == len(min_lis):
            #lis[i] = len(min_lis) + 1
            min_lis.append(a[i])
        else:
            #lis[i] = pos + 1
            min_lis[pos] = a[i]
        #print(*min_lis)
    return (len(min_lis))

print(LongestIncreasingSubsequence(num_list, n))

