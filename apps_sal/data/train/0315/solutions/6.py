class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y = y_x = 0
        res = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    x_y += 1
                else:
                    y_x += 1
        
        if (x_y + y_x) % 2 == 1:
            return -1
        
        res = x_y//2
        res += y_x//2
        
        if x_y % 2 == 1:
            res += 2
        return res

