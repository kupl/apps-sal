class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        s = K % 10
        s = str(s)
        if s in '024568':
            return -1
        else:
            i = 0
            s = 1
            while(i < 50000):
                if s % K == 0:
                    return len(str(s))
                s = (s * 10) + 1
                i += 1
