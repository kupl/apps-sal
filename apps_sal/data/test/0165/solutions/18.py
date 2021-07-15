import sys

fin = sys.stdin
fout = sys.stdout

b, s, d = list(map(int, fin.readline().split()))

wars = []


def nextDelta(dB, dS, dD):
    tempB = b + dB
    tempS = s + dS
    tempD = d + dD
    m = max(tempB, tempS, tempD)
    rz = 0
    rz += abs(m - tempB)
    rz += abs(m - tempS)
    rz += abs(m - tempD)
    wars.append(abs(rz))


nextDelta(1, 0, 1)
nextDelta(1, 1, 1)
nextDelta(2, 1, 1)
nextDelta(2, 2, 1)
nextDelta(1, 2, 1)
nextDelta(1, 1, 1)
nextDelta(2, 2, 2)
nextDelta(1, 2, 2)
nextDelta(1, 1, 2)
nextDelta(0, 0, 0)
fout.write(str(min(wars)))

