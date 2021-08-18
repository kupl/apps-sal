import math
import sys


def get_primes(n):
    result = set()
    while n % 2 == 0:
        result.add(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            result.add(i)
            n = n / i

    if n > 2:
        result.add(n)
    return list(result)


def calc(w, t, n):
    stack = []
    stack.append((t[0], dict([(p, [0]) for p in get_primes(w[0])])))
    max_length = 0
    visited = [False] * n
    visited[0] = True
    while stack:
        if stack[-1][0]:
            nxt = stack[-1][0][-1]
            stack[-1][0].pop()
            if visited[nxt]:
                continue
            else:
                visited[nxt] = True
            stack.append((t[nxt], dict([(p, [0]) for p in get_primes(w[nxt])])))
        else:
            last = stack[-1][1]
            stack.pop()
            if last:
                max_length = max(max_length, 1 + max([sum(v) for _, v in list(last.items())]))
            if stack:
                for k, v in list(last.items()):
                    if k in list(stack[-1][1].keys()):
                        stack[-1][1][k].append(max(v) + 1)
                        stack[-1][1][k].sort(reverse=True)
                        if len(stack[-1][1][k]) > 2:
                            del stack[-1][1][k][-1]
    return max_length


def __starting_point():
    n = int(input())
    weights = list(map(int, input().split()))
    lines = sys.stdin.readlines()
    tree = [[] for _ in range(n)]
    for line in lines:
        x, y = list(map(int, line.split()))
        tree[x - 1].append(y - 1)
        tree[y - 1].append(x - 1)

    print(calc(weights, tree, n))


__starting_point()
