N, A, B, C = map(int, input().split())
L = [0]*N
for i in range(N):
    L[i] = int(input())
INF = 10 ** 9


def dfs(times, a, b, c):  
    if times == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else INF
    no_pattern = dfs(times + 1, a, b, c)
    a_pattern = dfs(times + 1, a + L[times], b, c) + 10
    b_pattern = dfs(times + 1, a, b + L[times], c) + 10
    c_pattern = dfs(times + 1, a, b, c + L[times]) + 10

    return min(no_pattern, a_pattern, b_pattern, c_pattern)


print(dfs(0,0,0,0))
