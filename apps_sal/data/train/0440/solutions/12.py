class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        #if p > q: p = q + p%q
        start = [0, 'left', 'up']
        if q == p:
            return 1
        if q == 0:
            return 0
        num = 0
        while True:
            num = num + 1
            print(start)
            tmp = []
            if start[2] == 'up':
                if start[0] + q <= p:
                    if start[1] == 'left':
                        tmp = [start[0] + q, 'right', 'up']
                        if start[0] + q == p:
                            return 1
                    else:
                        tmp = [start[0] + q, 'left', 'up']
                        if start[0] + q == p:
                            return 2
                else:
                    if start[1] == 'left':
                        tmp = [2 * p - start[0] - q, 'right', 'down']
                    else:
                        tmp = [2 * p - start[0] - q, 'left', 'down']
            else:
                if start[0] - q >= 0:
                    if start[1] == 'left':
                        tmp = [start[0] - q, 'right', 'down']
                        if start[0] - q == 0:
                            return 0
                    else:
                        tmp = [start[0] - q, 'left', 'down']
                else:
                    if start[1] == 'left':
                        tmp = [q - start[0], 'right', 'up']
                        if start[0] - q == 0:
                            return 0
                    else:
                        tmp = [q - start[0], 'left', 'up']
            start = tmp
            # if num == 5:
            # break
