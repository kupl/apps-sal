class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        m = dict()
        for ind,num in enumerate(arr):
            if num in m:
                m[num].append(ind)
            else:
                m[num] = [ind]
        dp = []
        longest = 1
        for ind,num in enumerate(arr):
            if (num-difference) in m:
                possible_sol = []
                for diff_ind in m[num-difference]:
                    if diff_ind < len(dp):
                        possible_sol.append(dp[diff_ind] + 1)
                if possible_sol == []:
                    dp.append(1)
                else:
                    curr_max = max(possible_sol)
                    dp.append(curr_max)
                    if curr_max > longest:
                        longest = curr_max
                        
            else:
                dp.append(1)
        return longest
