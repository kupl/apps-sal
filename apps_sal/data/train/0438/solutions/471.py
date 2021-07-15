from sortedcontainers import SortedList

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        sizes = Counter((len(arr),))
        groups = SortedList([[1, len(arr)]])
        for i in range(len(arr)-1, -1, -1):
            if m in sizes:
                return i + 1
            n = arr[i]
            j = groups.bisect_left([n, n]) 
            if j == len(groups) or j > 0 and groups[j-1][1] >= n:
                j -= 1
            h, t = groups.pop(j)
            sizes[t - h + 1] -= 1
            if h < n: 
                groups.add([h, n-1])
                sizes[n-1 - h + 1] += 1 
            if t > n:    
                groups.add([n+1, t])
                sizes[t - n - 1 + 1] += 1 
        return -1 
