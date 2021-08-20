class Solution:

    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        states = set()
        for op_odd in [0, 1]:
            for op_even in [0, 1]:
                for op_third in [0, 1]:
                    op_all = m - op_odd - op_even - op_third
                    if op_all >= 0:
                        one = (op_odd + op_all + op_third) % 2
                        two = (op_even + op_all) % 2
                        three = op_odd % 2
                        four = (op_even + op_all + op_third) % 2
                        states.add((one, two, three, four)[:n])
        return len(states)
