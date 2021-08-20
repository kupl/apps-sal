import sys


def IN_I():
    return int(sys.stdin.readline().rstrip())


def IN_LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def IN_S():
    return sys.stdin.readline().rstrip()


def IN_LS():
    return list(sys.stdin.readline().rstrip().split())


N = IN_I()
a = [0] + IN_LI()
b = [0] * (N + 1)
ans = []
for i in range(N, 0, -1):
    tmp = 0
    for j in range(2 * i, N + 1, i):
        tmp += b[j]
    if tmp % 2 != a[i]:
        b[i] = 1
        ans.append(i)
if len(ans) == 0:
    print(0)
else:
    print(len(ans))
    print(' '.join(map(str, ans)))
