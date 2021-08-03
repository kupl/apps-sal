import sys
import os


def dfs(p, result, visited, start):
    q = [start]
    ret = None
    while len(q) > 0:
        s = q[len(q) - 1]
        if ret is not None:
            visited.remove(s)
            r = ret
            if r - 1 in visited:
                result[s] = s + 1
            else:
                result[s] = r
            q.pop()
            continue

        if result[s] > 0:
            ret = result[s]
            q.pop()
            continue
        if s in visited:
            ret = s + 1
            q.pop()
            continue

        next = p[s] - 1
        visited.add(s)
        q.append(next)


def solve(p):
    n = len(p)
    result = [-1] * n
    visited = set()
    for i in range(n):
        if i not in visited:
            dfs(p, result, visited, i)

    return result


def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(' '.join(map(str, solve(p))))


def __starting_point():
    main()


__starting_point()
