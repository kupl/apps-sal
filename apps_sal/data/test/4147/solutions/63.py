import sys
sys.setrecursionlimit(10**7)
n, A, B, C = map(int, input().split())
L_ls = [int(input()) for _ in range(n)]

# dfs(i,a,b,c) := i番目の竹のまえの時点で、A用の長さがa, B用の長さがb, C用の長さがcだった時の、それ以降の分岐での最初コスト


def dfs(i, a, b, c):
    if i == n:
        if a == 0 or b == 0 or c == 0:
            return float('inf')
        else:
            return abs(a - A) + abs(b - B) + abs(c - C)

    Min = dfs(i + 1, a, b, c)

    if a == 0:
        Min = min(Min, dfs(i + 1, a + L_ls[i], b, c))
    else:
        Min = min(Min, dfs(i + 1, a + L_ls[i], b, c) + 10)

    if b == 0:
        Min = min(Min, dfs(i + 1, a, b + L_ls[i], c))
    else:
        Min = min(Min, dfs(i + 1, a, b + L_ls[i], c) + 10)

    if c == 0:
        Min = min(Min, dfs(i + 1, a, b, c + L_ls[i]))
    else:
        Min = min(Min, dfs(i + 1, a, b, c + L_ls[i]) + 10)

    return Min


print(dfs(0, 0, 0, 0))
