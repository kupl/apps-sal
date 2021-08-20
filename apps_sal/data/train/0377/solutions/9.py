class Solution:

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        import math
        if A % B == 0 or B % A == 0:
            return N * min(A, B) % (10 ** 9 + 7)
        testRange = (1, N * min(A, B))
        testValue = int((testRange[1] + testRange[0]) / 2)
        magicNums = math.floor(testValue / A) + math.floor(testValue / B) - math.floor(testValue * math.gcd(A, B) / (A * B))
        while magicNums != N:
            testRange = (testRange[0], testValue) if magicNums > N else (testValue, testRange[1])
            testValue = math.ceil((testRange[1] + testRange[0]) / 2)
            magicNums = math.floor(testValue / A) + math.floor(testValue / B) - math.floor(testValue * math.gcd(A, B) / (A * B))
        return max(int(testValue / A) * A, int(testValue / B) * B) % (10 ** 9 + 7)
