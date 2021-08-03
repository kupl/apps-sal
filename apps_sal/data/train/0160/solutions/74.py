class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles) // 2
        dp1 = [0] * (N + 1)
        dp2 = [0] * (N + 1)

        rot = 0
        temp = piles.copy()

        i = 1
        while len(temp) > 0:
            alex = max(temp[0], temp[-1])
            if temp[0] == temp[-1]:
                rot += 1
            if alex == temp[0]:
                dp1[i] = dp1[i - 1] + temp[0]
                temp.pop(0)
            else:
                dp1[i] = dp1[i - 1] + temp[-1]
                temp.pop()
            print(alex)
            print(temp)
            lee = max(temp[0], temp[-1])
            if temp[0] == temp[-1]:
                rot += 1

            if lee == temp[0]:
                dp2[i] = dp2[i - 1] + temp[0]
                temp.pop(0)
            else:
                dp2[i] = dp2[i - 1] + temp[-1]
                temp.pop()
            print(lee)
            print(temp)
            i += 1
        print(dp1)
        print(dp2)

        if rot > 0:
            return True
        return dp1[-1] > dp2[-1]
