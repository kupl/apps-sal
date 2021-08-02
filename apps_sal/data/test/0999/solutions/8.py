from sys import stdin, stdout

n = int(stdin.readline())
chessStart = []
chessEnd = []
for i in range(n):
    l, r = list(map(int, stdin.readline().rstrip().split()))
    chessStart.append(l)
    chessEnd.append(r)

m = int(stdin.readline())
programStart = []
programEnd = []
for i in range(m):
    l, r = list(map(int, stdin.readline().rstrip().split()))
    programStart.append(l)
    programEnd.append(r)

chessEarlyEnd = min(chessEnd)
chessLateStart = max(chessStart)
programEarlyEnd = min(programEnd)
programLateStart = max(programStart)

bestCase = max([chessLateStart - programEarlyEnd, programLateStart - chessEarlyEnd])
print(max([0, bestCase]))
