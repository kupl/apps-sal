class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        self.n = len(result)
        self.levels = []
        self.alldigit = {}
        self.allch = []
        self.result = result
        self.nonzero = set()
        for w in words:
            self.nonzero.add(w[0])
        self.nonzero.add(result[0])
        for r in range(len(result)):
            l = []
            for w in words:
                if r < len(w):
                    l.append(w[len(w) - r - 1])

            l.append(result[len(result) - 1 - r])
            self.levels.append(l)
        self.occupy = set()
        self.checkdigit = {}

        if len(self.levels[-1]) == 1:
            self.alldigit[self.levels[-1][0]] = 1
            self.occupy.add(1)

        for l in range(len(self.levels)):
            newch = set(self.levels[l]) - set(self.allch)
            self.allch.extend(newch)
            self.checkdigit[len(self.allch)] = l + 1
        if self.tryone(0, len(self.allch)):
            return True
        else:
            return False

    def tryone(self, level, maxl):
        flag = False
        if maxl == level:
            if self.check(self.checkdigit[level]):
                return True
            else:
                return False
        if level in self.checkdigit:
            if not self.check(self.checkdigit[level]):
                return False
            else:
                pass

        if self.allch[level] in self.alldigit:
            if self.tryone(level + 1, maxl):
                return True
            else:
                return False

        for i in range(10):
            if i not in self.occupy:
                if i != 0 or self.allch[level] not in self.nonzero:
                    self.occupy.add(i)
                    self.alldigit[self.allch[level]] = i
                    if self.tryone(level + 1, maxl):
                        return True
                    del self.alldigit[self.allch[level]]
                    self.occupy.remove(i)
        return False

    def check(self, level):
        plus = 0
        for i in range(level):
            levelsum = 0
            for j in range(len(self.levels[i]) - 1):
                levelsum += self.alldigit[self.levels[i][j]]
            if (levelsum + plus) % 10 != self.alldigit[self.levels[i][-1]]:
                return False
            else:
                plus = int((levelsum + plus) / 10)
        return True
