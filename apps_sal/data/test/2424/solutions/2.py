import sys


def input():
    return sys.stdin.readline().rstrip()


P = 998244353
N = int(input())
X = [0] * 1001001
A = [[int(a) for a in input().split()[1:]] for _ in range(N)]
for i in range(N):
    for a in A[i]:
        X[a] += 1
ans = 0
for i in range(N):
    ans = (ans + sum([X[a] for a in A[i]]) * pow(len(A[i]), P - 2, P)) % P
print(ans * pow(N * N, P - 2, P) % P)
