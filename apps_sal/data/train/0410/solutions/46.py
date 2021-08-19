class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        dic = {}

        def determine_power(a):
            power = 0
            while a > 1:
                if a % 2:
                    a = 3 * a + 1
                    power += 1
                else:
                    a = a / 2
                    power += 1
            return power
        for element in range(lo, hi + 1):
            p = determine_power(element)
            dic.update({element: p})
        dd = sorted(list(dic.items()), key=lambda x: x[1])
        return dd[k - 1][0]
