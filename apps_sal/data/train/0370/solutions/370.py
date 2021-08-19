class Solution:

    def find_common_fractor(self, num: int, u):
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                u.union(num, i)
                u.union(num, num // i)

    def largestComponentSize(self, A: List[int]) -> int:
        u = UnionFind(max(A) + 1)
        for item in A:
            self.find_common_fractor(item, u)
        o = 1
        temp_dict = {}
        for item in A:
            parent = u.find(item)
            if parent not in temp_dict:
                temp_dict[parent] = 1
            else:
                temp_dict[parent] += 1
            o = max(o, temp_dict[parent])
        return o


class UnionFind:

    def __init__(self, len_: int):
        self.lst = [i for i in range(len_)]

    def find(self, num: int):
        if num != self.lst[num]:
            self.lst[num] = self.find(self.lst[num])
        return self.lst[num]

    def union(self, x: int, y: int):
        self.lst[self.find(x)] = self.lst[self.find(y)]
