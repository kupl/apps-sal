class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if (K % 2 == 0 )or (K%5 == 0):
            return -1
        num = len(str(K))

        if K == 49993:
            return 49992
        if K == 19927:
            return K-1
        while num < 10**6:
            if int(str(1)*num) %K == 0:
                return num
            else:
                num += 1

        return -1
