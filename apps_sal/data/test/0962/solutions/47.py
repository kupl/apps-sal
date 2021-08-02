import sys
sys.setrecursionlimit(10**7)


def main():
    N, M = list(map(int, input().split()))
    V = [[] for _ in range(N)]
    for _ in range(M):
        a, b = list(map(int, input().split()))
        V[a - 1].append(b - 1)
    C = [0] * N

    def dfs(n):
        if C[n] == 2:
            return False
        if C[n] == 1:
            return True
        C[n] = 1
        for i in V[n]:
            if dfs(i):
                return True
        C[n] = 2
        return False
    for i in range(N):
        if dfs(i):
            return 0
    return -1


print((main()))
