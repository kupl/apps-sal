from collections import defaultdict
from collections import deque
from sys import stdin
lines = deque((line.strip() for line in stdin.readlines()))


def nextline():
    return lines.popleft()


def types(cast):
    return tuple((int(x) for x in nextline().split()))


def ints():
    return types(int)


def strs():
    return nextline().split()


def main():
    n = int(nextline())
    graph = defaultdict(list)
    for _ in range(1, n):
        (a, b) = ints()
        graph[a].append(b)
        graph[b].append(a)
    stack = [(1, 1, 0)]
    visited = set()
    expected = 0
    while stack:
        (city, denominator, length) = stack.pop()
        visited.add(city)
        choices = [choice for choice in graph[city] if choice not in visited]
        if choices:
            for choice in choices:
                stack.append((choice, denominator * len(choices), length + 1))
        else:
            expected += length / denominator
    print(expected)


def __starting_point():
    main()


__starting_point()
