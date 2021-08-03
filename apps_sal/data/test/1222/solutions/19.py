N = int(input()) + 1
Ans = []


def dfs(depth, p):
    if depth == 0:
        Ans.append(p)
        if len(Ans) == N:
            print(p)
            return
        return
    if p != 0:
        for digit in range(max(0, p % 10 - 1), min(10, p % 10 + 2)):
            dfs(depth - 1, p * 10 + digit)
    else:
        for digit in range(10):
            dfs(depth - 1, p * 10 + digit)


dfs(10, 0)
