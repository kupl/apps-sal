class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort()
        dic = {}
        for i in A:
            if i % 2 == 0 and i/2 in dic:
                i = i / 2
                dic[i] -= 1
                if dic[i] == 0:
                    del dic[i]
            elif i * 2 in dic:
                i = i * 2
                dic[i] -= 1
                if dic[i] == 0:
                    del dic[i]
            else:
                dic[i] = dic.setdefault(i, 0) + 1
                continue
        return len(dic) == 0
