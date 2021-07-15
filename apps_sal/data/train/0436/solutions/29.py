class Solution:
    def minDays(self, n: int) -> int:
        dic = {n:0}
        while 0 not in dic:
            tmp = {}
            for m in dic:
                tmp[m-1] = min(dic[m-1],dic[m]+1) if m-1 in dic else dic[m] + 1
                if m % 2 == 0: tmp[m//2] = min(dic[m//2],dic[m]+1) if m//2 in dic else dic[m] + 1
                if m % 3 == 0: tmp[m//3] = min(dic[m//3],dic[m]+1) if m//3 in dic else dic[m] + 1
            dic = tmp
        return dic[0]

