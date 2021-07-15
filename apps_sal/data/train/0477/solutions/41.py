class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def reverseInvert(string: str) -> str:
            output = []
            for char in string:
                if char == '0':
                    output.append('1')
                else:
                    output.append('0')
            output.reverse()
            return ''.join(output)
            
        def getNthSequence(n: int) -> str:
            if n == 1:
                return '0'
            prev = getNthSequence(n-1)
            return prev + '1' + reverseInvert(prev)
        
        return getNthSequence(int(ceil(log2(k)) + 1))[k-1]

