import sys
sys.setrecursionlimit(10**7)

def main():
    N, M = list(map(int, input().split()))
    C = [[] for _ in range(N)]
    for _ in range(M):
        l, r, d = list(map(int, input().split()))
        C[l - 1].append((r - 1, d))
        C[r - 1].append((l - 1, -d))
    INF = 10 ** 10
    P = [INF] * N
    def dfs(n, p, f):
        if P[n] != INF:
            if P[n] != p:
                return False
            return True
        P[n] = p
        for i, d in C[n]:
            if i == f:
                continue
            if not dfs(i, p + d, n):
                return False
        return True
            
    for i in range(N):
        if P[i] != INF:
            continue
        if not dfs(i, 0, -1):
            return False
    return True

print(('Yes' if main() else 'No'))

