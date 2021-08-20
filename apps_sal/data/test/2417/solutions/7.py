import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
A = [int(a) - 1 for a in input().split()][::-1]
C = [-1] * N
for i in range(N):
    C[A[i]] = i
B = [C[int(a) - 1] for a in input().split()][::-1]
(ans, ma) = (0, -1)
for i in B:
    if ma > i:
        ans += 1
    ma = max(ma, i)
print(ans)
