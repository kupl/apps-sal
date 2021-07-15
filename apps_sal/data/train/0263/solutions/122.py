#https://leetcode-cn.com/problems/knight-dialer/solution/4zhuang-tai-dong-tai-gui-hua-pythonjie-kong-jian-f/ markov chain, 这个解法神了
class Solution:
    def knightDialer(self, N: int) -> int:
        if N ==1 : return 10
        
        nums = [1,1,1,1]
        
        for _ in range(N-1):
            nums = [nums[1] + nums[2], 2 * nums[0], 2 * nums[0] + nums[3], 2 * nums[2]]
        
        return (4 * nums[0] + 2 * nums[1] + 2 * nums[2] + nums[3]) % (10**9+7)

