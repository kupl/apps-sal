class LinkedList:

    def __init__(self):
        self.map = {}
        self.min = -1
        self.max = -1

    def add_to_key(self, key):
        if key in self.map:
            self.map[key][0] += 1
            new_key = self.map[key][1]
            while new_key >= 1 and self.map[key][0] > self.map[new_key][0]:
                (self.map[key][1], self.map[new_key][1]) = (self.map[new_key][1], key)
                (self.map[new_key][2], self.map[key][2]) = (self.map[key][2], new_key)
                if self.map[new_key][2] > 0:
                    self.map[self.map[new_key][2]][1] = new_key
                if self.min == key:
                    self.min = new_key
                new_key = self.map[key][1]
            if new_key >= 1:
                self.map[new_key][2] = key
        else:
            self.map[key] = [1, self.min, -1]
            if self.min > 0:
                self.map[self.min][2] = key
            self.min = key
        if self.max <= 0 or self.map[self.max][0] < self.map[key][0]:
            self.max = key

    def check(self):
        A = self.biggest()
        B = self.smallest()
        if A == 1:
            return True
        elif B == 1:
            C = self.unique_min()
            if not C:
                if A == 2 and self.unique_max():
                    return True
                else:
                    return False
            else:
                next_min = self.map[self.min][1]
                if self.map[next_min][0] == A:
                    return True
                else:
                    return False
        else:
            D = self.unique_max()
            if D:
                return A == B + 1 or A == B
            else:
                return False

    def smallest(self):
        if self.min == -1:
            return 0
        else:
            return self.map[self.min][0]

    def biggest(self):
        if self.max == -1:
            return 0
        else:
            return self.map[self.max][0]

    def unique_min(self):
        if self.min <= 0:
            return True
        else:
            next_min = self.map[self.min][1]
            return next_min >= 1 and self.map[self.min][0] != self.map[next_min][0]

    def unique_max(self):
        if self.max <= 0:
            return True
        else:
            next_max = self.map[self.max][2]
            if next_max > 0:
                return self.map[self.max][0] != self.map[next_max][0]
            else:
                return True


class Solution:

    def maxEqualFreq(self, nums: List[int]) -> int:
        out = LinkedList()
        result = 2
        for (length, num) in enumerate(nums):
            out.add_to_key(num)
            if out.check():
                result = length + 1
        return result
