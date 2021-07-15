# 10th finish 14:18

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ['0']
        for i in range(n-1):
            temp1 = s.copy()
            for i in range(len(temp1)):
                if temp1[i] == '0':
                    temp1[i] = '1'
                elif temp1[i] == '1':
                    temp1[i] = '0'
            temp1.reverse()
            temp = s + ['1'] + temp1
            s = temp
        # print(s)
        return s[k-1]
