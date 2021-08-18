class Game123:
    def __init__(self):
        self.alice = [0] * 9
        self.bob = [0] * 9
        self.moves = [-1] * 10
        self.count = 0
        self.pointsA = 0
        self.pointsB = 0

    def gameChoice(self, m, r, bBob):
        choice = self.alice
        if bBob:
            choice = self.bob
        for i in range(len(m)):
            choice[3 * r + i] = m[i]

    def findMove(self, a, b):
        m = (a - 1) * 3 + b - 1
        for i in range(self.count):
            if self.moves[i] == m:
                return i
        self.moves[self.count] = m
        self.count += 1
        return -1

    def computePoints(self, m):
        b = m % 3 + 1
        a = m // 3 + 1
        if a == b:
            return
        if a == 3 and b == 2 or a == 2 and b == 1 or a == 1 and b == 3:
            self.pointsA += 1
        else:
            self.pointsB += 1

    def output(self):
        print("{0} {1}".format(self.pointsA, self.pointsB))

    def startGame(self, a, b, totalmoves):
        found = -1
        while found < 0:
            found = self.findMove(a, b)
            m = (a - 1) * 3 + b - 1
            a = self.alice[m]
            b = self.bob[m]
        pointaA = 0
        pointsB = 0
        if totalmoves <= self.count:
            for i in range(totalmoves):
                self.computePoints(self.moves[i])
        else:
            totalmoves -= found
            repeats = totalmoves // (self.count - found)
            totalmoves %= (self.count - found)
            for i in range(found, self.count):
                self.computePoints(self.moves[i])
            self.pointsA *= repeats
            self.pointsB *= repeats
            for i in range(found):
                self.computePoints(self.moves[i])
            for i in range(found, totalmoves + found):
                self.computePoints(self.moves[i])
        self.output()

    def test():
        g = Game123()
        g.gameChoice([2, 2, 1], 0, False)
        g.gameChoice([3, 3, 1], 1, False)
        g.gameChoice([3, 1, 3], 2, False)
        g.gameChoice([1, 1, 1], 0, True)
        g.gameChoice([2, 1, 1], 1, True)
        g.gameChoice([1, 2, 3], 2, True)
        g.startGame(1, 1, 8)


def nia():
    s = input()
    while len(s) == 0:
        s = input()
    s = s.split()
    iVal = []
    for i in range(len(s)):
        iVal.append(int(s[i]))
    return iVal


def solve():
    g = Game123()
    nab = nia()
    for i in range(3):
        g.gameChoice(nia(), i, False)
    for i in range(3):
        g.gameChoice(nia(), i, True)
    g.startGame(nab[1], nab[2], nab[0])


solve()
