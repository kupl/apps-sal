import sys


class MyReader:

    def __init__(self):
        filename = 'file.in'
        if self.isLocal():
            self.file = open(filename)
        self.str = ['']
        self.ind = 1

    def isLocal(self):
        return len(sys.argv) > 1 and sys.argv[1] == 'SCHULLZ'

    def nextString(self):
        if self.isLocal():
            return self.file.read()
        else:
            return input()

    def nextInt(self):
        return int(self.nextToken())

    def nextToken(self):
        if self.ind >= len(self.str):
            self.ind = 0
            self.str = self.nextString().split()
        self.ind += 1
        return self.str[self.ind - 1]


def SoLvE():
    rdr = MyReader()
    n = rdr.nextInt()
    m = rdr.nextInt()
    if n // m < 3:
        print(-1)
        return
    a = []
    for i in range(0, n):
        a.append(-1)
    cur = 0
    for i in range(0, m):
        a[cur] = i + 1
        cur += 1
    for i in range(0, m):
        a[cur] = i + 1
        cur += 1
    for i in range(0, m - 1):
        a[cur] = i + 2
        cur += 1
    a[cur] = 1
    cur += 1
    for cc in range(cur, n):
        a[cc] = cc % m + 1
        cc += 1
    for i in range(0, n):
        sys.stdout.write(str(a[i]))
        sys.stdout.write(' ')
    sys.stdout.flush()


SoLvE()
