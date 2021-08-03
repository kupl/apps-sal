import sys

sys.setrecursionlimit(10 ** 9)

S = input()
K = int(input())

chars = sorted(set(S))
checked = set()


def dfs(s):
    for c in chars:
        if len(checked) >= K:
            return
        next_s = s + c
        if next_s not in checked and next_s in S:
            checked.add(next_s)
            if len(checked) == K:
                print(next_s)
                return
            elif len(next_s) <= len(S):
                dfs(next_s)


dfs('')
