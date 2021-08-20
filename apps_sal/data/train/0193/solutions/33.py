import collections


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        lst = []
        dic = collections.Counter(arr)
        keys = sorted(dic, key=lambda x: dic[x], reverse=True)
        for n in keys:
            if len(lst) >= len(arr) // 2:
                return len(set(lst))
            else:
                for _ in range(dic[n]):
                    lst.append(n)
        if len(lst) >= len(arr) // 2:
            return len(set(lst))
