def dfs(curr_index, n, rollMax, prev, d):
        if curr_index == n:
            return 1
        if curr_index > n:
            return 0
        if (curr_index, prev) in d:
            return d[(curr_index, prev)]
        count = 0
        for i in range(6):
            if i!=prev:
                for repeat in range(1, rollMax[i]+1):
                    count+=dfs(curr_index+repeat, n, rollMax, i, d)
            d[(curr_index,prev)] = count
                
        return count
    
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        d = {}
        MOD = 1000000007
        return dfs(0, n, rollMax, -1,d)%MOD
