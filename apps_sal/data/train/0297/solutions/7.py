class Solution:
    def __init__(self):
        self.total = 0
        self.string = []
        self.dict_ = {}
        self.arr = []
        self.n = 0

    def perm(self):
        if(self.n == len(self.string)):
            self.total += 1

        for i in range(len(self.arr)):
            if(self.arr[i][1] > 0):
                self.arr[i][1] -= 1
                self.string.append(self.arr[i][0])
                self.perm()
                self.string.pop()
                self.arr[i][1] += 1

    def numTilePossibilities(self, tiles: str) -> int:
        for string in tiles:
            if string in self.dict_:
                self.dict_[string] += 1
            else:
                self.dict_[string] = 1

        for key in self.dict_:
            temp = [key, self.dict_[key]]
            self.arr.append(temp)

        for i in range(1, len(tiles) + 1):
            self.n = i
            self.perm()
        return self.total
