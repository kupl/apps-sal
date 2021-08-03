class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        pre = -1
        ans = a = b = 0
        x = y = -1
        for cur in tree:
            if cur != x and cur != y:
                x, y = pre, cur
                a, b = b, 1
            elif cur == pre:
                b += 1
            else:
                a += b
                b = 1
            if a + b > ans:
                ans = a + b
            pre = cur
        return ans
