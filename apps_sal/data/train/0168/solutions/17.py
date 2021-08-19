class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if len(s) < k:
            return False

        dic = {}
        for sym in s:
            if sym in dic.keys():
                dic[sym] = 1 - dic[sym]
            else:
                dic[sym] = 1

        # num=sum(dic.values())
        num = 0
        for i in dic.values():
            num += i

        if num <= k:
            return True
        else:
            return False
