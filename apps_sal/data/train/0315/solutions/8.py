class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        a = 0
        b = 0
        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y' :
                a += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                b += 1
                     
        if a % 2 == 0 and b % 2 == 0:
            return a // 2 + b // 2 
        elif a % 2 == 1 and b % 2 == 1:
            return a // 2 + b // 2 + 2 
        else:
            return -1

