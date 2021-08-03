import sys
def read(): return sys.stdin.readline().rstrip()
def readi(): return int(sys.stdin.readline())
def writeln(x): return sys.stdout.write(str(x) + "\n")
def write(x): return sys.stdout.write(x)


def getM(k, l):
    if k == 0:
        return 0
    if l >= 2 * k:
        return 2 * k
    else:
        return l


def getO(k, l):
    if k == 0:
        return 0
    if l >= k:
        return k
    else:
        return l


N, F = list(map(int, read().split()))
days = []
for i in range(N):
    K, L = list(map(int, read().split()))
    M = getM(K, L)
    O = getO(K, L)
    days.append((M - O, M, O))
days.sort(key=lambda x: x[0])
sm = 0
for i in range(F):
    _, m, _ = days[-1 - i]
    sm += m
for i in range(N - F):
    _, _, o = days[-1 - F - i]
    sm += o
writeln(sm)
