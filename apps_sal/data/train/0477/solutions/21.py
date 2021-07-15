def invert(s):
    return (bin(int(s, 2)^int('1'*len(s), 2)))[2:]

def reverse(s):
    return s[::-1]

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        S = [None]*n
        S[0] = '0'
        for i in range(1, n):
            S[i] = S[i-1] + '1' + reverse(invert(S[i-1]))
        
        return S[n-1][k-1]
