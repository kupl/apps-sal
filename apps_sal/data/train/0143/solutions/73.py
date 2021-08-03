from collections import Counter


class window:

    def __init__(self):
        self.type = Counter()

    def add(self, x):
        self.type[x] += 1

    def remove(self, x):
        self.type[x] -= 1
        if self.type[x] == 0:
            del self.type[x]

    def valid(self):
        return len(self.type) <= 2


class Solution:
    def totalFruit(self, tree):

        win = window()
        l, res = 0, 0
        for r, fruit in enumerate(tree):
            win.add(fruit)
            while l < r and not win.valid():
                win.remove(tree[l])
                l += 1
            res = max(res, r - l + 1)
        return res
