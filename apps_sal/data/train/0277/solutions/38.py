class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        if len(light) == 0:
            return 0
        dic = {}
        count = 0
        flag = True
        Max = light[0]
        for i, item in enumerate(light):
            dic[item] = True
            Max = max(light[i], Max)
            if Max == len(dic):
                count += 1
                continue
            elif Max > len(dic):
                flag = False
            else:
                for j in range(item, 0, -1):
                    if j not in dic:
                        flag = False
            if flag:
                count += 1
            flag = True
        return count

