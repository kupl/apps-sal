class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        def roll(last, last_num, rolls):
            if rolls == 0:
                return 1
            if (last, last_num, rolls) in memo:
                return memo[(last, last_num, rolls)]
            tmp = 0
            for cur in range(1, 7):
                if cur == last:
                    if last_num + 1 > rollMax[cur - 1]:
                        continue
                    tmp += roll(last, last_num + 1, rolls - 1)
                else:
                    tmp += roll(cur, 1, rolls - 1)
                tmp = tmp % (10**9 + 7)
            memo[(last, last_num, rolls)] = tmp
            return tmp

        memo = {}
        return roll(-1, 0, n)
