class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        x, y = p, q
        m = -q / p
        wall = 1
        while 1:
            b = y - m * x
            # print(x, y, m, b, wall)
            # y = m * x + b
            flag = 0
            if flag == 0 and wall != 0:
                # y = 0
                temp = x
                x = -b / m
                if 0 <= x <= p:
                    flag = 1
                    y = 0
                    wall = 0
                else:
                    x = temp
            if flag == 0 and wall != 2:
                # y = p
                temp = x
                x = (p - b) / m
                if 0 <= x <= p:
                    flag = 1
                    y = p
                    wall = 2
                else:
                    x = temp
            if flag == 0 and wall != 3:
                # x = 0
                temp = y
                y = b
                if 0 <= y <= p:
                    flag = 1
                    x = 0
                    wall = 3
                else:
                    y = temp
            if flag == 0 and wall != 1:
                # x = p
                temp = y
                y = m * p + b
                if 0 <= y <= p:
                    flag = 1
                    x = p
                    wall = 1
                else:
                    y = temp
            if (round(x, 2), round(y,2)) == (p, 0):
                return 0
            if (round(x, 2), round(y,2)) == (p, p):
                return 1
            if (round(x, 2), round(y,2)) == (0, p):
                return 2
            m = -m

