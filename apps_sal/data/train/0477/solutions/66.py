class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(l):
            result = []
            for item in l:
                if item == '0':
                    result.append('1')
                else:
                    result.append('0')
            return result

        string = '0'
        while len(string) < k:
            string = string + '1'
            addition = invert(string[0:len(string) - 1])
            addition.reverse()
            addition = ''.join(addition)
            string = string + addition

        return string[k - 1]
