class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        memo = {0:1, 1:0}
        cnt = 0
        curr_sum = 0
        K = 10**9+7
        for n in arr:
            curr_sum += n
            if curr_sum%2==0:
                cnt += memo[1]
            else:
                cnt += memo[0]
            memo[curr_sum%2] += 1
            cnt = cnt%K
            # print (memo, cnt)
        return cnt
