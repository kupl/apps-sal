import sys


def IN_I():
    return int(sys.stdin.readline().rstrip())


def IN_LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def IN_S():
    return sys.stdin.readline().rstrip()


def IN_LS():
    return list(sys.stdin.readline().rstrip().split())


INF = float('inf')
MOD = 10 ** 9 + 7
N = IN_I()
A = IN_LI()
for i in range(N):
    A[i] -= i + 1
A.sort()
if N % 2 == 1:
    b = A[N // 2]
else:
    b = (A[N // 2 - 1] + A[N // 2]) // 2
ans = 0
for a in A:
    ans += abs(a - b)
print(ans)
