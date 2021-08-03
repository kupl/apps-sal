class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        '''m = set()
        flag, c = -1, 0
        for i in range(len(light)):
            m.add(light[i])
            for j in range(i+1,0,-1):
                if j not in m:
                    flag = 1
                    break
            if flag == 1:
                flag = -1
            else:
                c += 1
        return c'''
        res = 0
        curr = -1
        for p, q in enumerate(light):
            curr = max(curr, q)
            if curr == p + 1:
                res += 1
        return res
