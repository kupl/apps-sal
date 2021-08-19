class Solution:

    def minSteps(self, s: str, t: str) -> int:
        s = list(s)
        t = list(t)
        dic = dict()
        for i in s:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        print(dic)
        for j in t:
            if j in dic:
                dic[j] = dic[j] - 1
        print(dic)
        sum = 0
        for i in list(dic.values()):
            if i > 0:
                sum += i
        return sum
