import sys


class MyReader:
    #    file = null;
    def __init__(self):
        filename = "file.in"
        if self.isLocal():
            self.file = open(filename)
        self.str = [""]
        self.ind = 1

    def isLocal(self):
        return len(sys.argv) > 1 and sys.argv[1] == "SCHULLZ"

    def nextString(self):
        if self.isLocal():
            return self.file.read()
        else:
            return input()

    def nextInt(self):
        return int(self.nextToken())

    def nextToken(self):
        if (self.ind >= len(self.str)):
            self.ind = 0
            self.str = self.nextString().split()
        self.ind += 1
        return self.str[self.ind - 1]


rdr = MyReader()

n = rdr.nextInt()
m = rdr.nextInt()


a = [[0 for x in range(m)] for y in range(n)]


for i in range(0, n):
    for j in range(0, m):
        a[i][j] = rdr.nextInt()

was = []
MX = 200500
for i in range(0, MX):
    was.append(False)

for i in range(2, MX):
    if was[i] == False:
        for j in range(i + i, MX, i):
            was[j] = True
was[1] = True
was[0] = True
nxt = []
for i in range(0, MX):
    nxt.append(-1)

prev = -1
for i in range(MX - 1, -1, -1):
    if was[i] == False:
        prev = i
    nxt[i] = prev


res = MX * 505

for i in range(0, n):
    tres = 0
    for j in range(0, m):
        tres += nxt[a[i][j]] - a[i][j]
    res = min(res, tres)

for j in range(0, m):
    tres = 0
    for i in range(0, n):
        tres += nxt[a[i][j]] - a[i][j]
    res = min(res, tres)

assert(res != MX * 505)
print(res)
