class Solution:
    def getProbability(self, balls: List[int]) -> float:
        '''
        箱子中有n个球，箱中有2种颜色的球，分别有k1,k2个
        箱子中的组合数为n!/k1!k2!
        每次选取同一色彩的所有球分开放入两个盒子中
        '''
        k = len(balls)  # 总色彩数
        n = sum(balls)  # 总球数
        total = 0  # 总组合数
        valid = 0  # 符合条件总数
        fact = [1] * 50
        for i in range(1, 50):
            fact[i] = i * fact[i - 1]

        def dfs(d, b1, b2, c1, c2, p1, p2):
            nonlocal total
            nonlocal valid
            if b1 > n // 2 or b2 > n // 2:
                return
            if d == k:
                count = fact[b1] / p1 * fact[b2] / p2
                total += count
                valid += count * (c1 == c2)
                return
            for s1 in range(balls[d] + 1):
                s2 = balls[d] - s1
                dfs(d + 1, b1 + s1, b2 + s2, c1 + (s1 > 0), c2 + (s2 > 0), p1 * fact[s1], p2 * fact[s2])
        dfs(0, 0, 0, 0, 0, 1, 1)
        return valid / total
