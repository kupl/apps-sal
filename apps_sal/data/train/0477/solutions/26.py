class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse_invert(array: List[str]) -> List[str]:
            res = []
            for ind in range(len(array)-1, -1, -1):
                res.append('1' if array[ind] == '0' else '0')
            return res
        
        bits = ['0']
        for curr in range(2, n+1):
            bits += ['1'] + reverse_invert(bits)
        return bits[k-1]
