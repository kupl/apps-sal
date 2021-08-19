class Solution:

    def findKthBit(self, n: int, k: int) -> str:

        def invert(data):
            ans = ''
            for val in data:
                ans += '1' if val == '0' else '0'
            return ans
        output = '0'
        for i in range(1, n + 1):
            output += '1' + invert(output)[::-1]
            if len(output) >= k:
                break
        return output[k - 1]
