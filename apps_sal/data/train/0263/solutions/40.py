class Solution:
    def knightDialer(self, n: int) -> int:
        
        move = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9],5:[],6:[1,7,0],7:[2,6],8:[1,3],9:[4,2]}
        
        pre = [1 for _ in range(10)]
        for i in range(n-1):
            new = [0 for _ in range(10)]
            for j in range(10):
                for k in move[j]:
                    new[k] += pre[j]%(10**9+7)
            pre = new
        
        return sum(pre)%(10**9+7)

