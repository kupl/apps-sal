class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        l = len(str(K))
        m = ['1'] * l
        s = ''.join(m)
        n = int(s)
        while True:
            if n % K == 0:
                return len(str(n))
            n = n * 10 + 1
        return -1
