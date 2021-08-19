class Solution:
    def knightDialer(self, N: int) -> int:
        res = [1] * 10  # 每个位置出现的次数
        next_move = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        i = 1
        while i < N:
            res2 = [0] * 10
            for k, v in enumerate(res):
                for j in next_move[k]:  # 对于跳到的下一个位置，更新出现的次数
                    res2[j] += v
            res = res2  # 更新结果
            i += 1
        return sum(res) % (10**9 + 7)  # 不要忘记取余
# https://www.jianshu.com/p/caa2c35321a7
