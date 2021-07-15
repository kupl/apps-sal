import sys


def IN_I(): return int(sys.stdin.readline().rstrip())
def IN_LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def IN_S(): return sys.stdin.readline().rstrip()
def IN_LS(): return list(sys.stdin.readline().rstrip().split())


N = IN_I()
A = IN_LI()

b = [0] * N
S = sum(A)
b[0] = S - 2 * sum(A[1::2])

for i in range(1, N):
    b[i] = 2 * A[i - 1] - b[i - 1]

print((' '.join(map(str, b))))


