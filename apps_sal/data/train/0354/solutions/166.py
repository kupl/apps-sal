class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        cach = {}

        def helper(remain, last, rollMax):
            if (remain, last) in cach:
                return cach[remain, last]
            else:
                if remain == 0:
                    return 1
                else:
                    ret = 0
                    for i in range(6):
                        if last == i:
                            continue
                        else:
                            for j in range(rollMax[i]):
                                if remain - j - 1 >= 0:
                                    ret += helper(remain - j - 1, i, rollMax)
                cach[remain, last] = ret % 1000000007
                return cach[remain, last]
        return helper(n, -1, rollMax)
