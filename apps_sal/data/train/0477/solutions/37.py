class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        memo_table = [''] * (n)

        memo_table[0] = '0'

        for i in range(1, n):
            memo_table[i] = self.new_level(memo_table[i - 1])

        return memo_table[n - 1][k - 1]

    def new_level(self, old_level: str):
        new_level = ['1'] * (len(old_level) * 2 + 1)
        left = 0
        right = len(old_level) * 2
        for c in old_level:
            new_level[left] = c
            if c == '0':
                new_level[right] = '1'
            else:
                new_level[right] = '0'
            left += 1
            right -= 1

        return ''.join(new_level)
