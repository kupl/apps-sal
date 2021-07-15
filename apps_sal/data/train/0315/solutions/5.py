class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x = 0
        y = 0
        
        for index in range(0, len(s1)):
            if s1[index] != s2[index]:
                if s1[index] == 'x':
                    x += 1
                else:
                    y += 1
        
        
        mid = ( x + y ) / 2
        x, y = x % 2, y % 2
        
        if x + y == 1:
            return -1
        
        if x + y == 2:
            mid += 1
        
        print(mid)
        return int(mid)

