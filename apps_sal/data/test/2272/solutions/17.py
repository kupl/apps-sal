from collections import deque

def solve():
    t = int(input().rstrip())
    nodes = []
    graph = {}
    for _ in range(t):
        k, x, y = list(map(int, input().rstrip().split()))
        if k == 1:
            nodes.append((x,y)) 
            if (x,y) not in graph:
                graph[(x,y)] = []
            for a, b in graph:
                if a < x < b or a < y < b:
                    graph[(x,y)].append((a,b))
                if x < a < y or x < b < y:
                    graph[(a,b)].append((x,y))
        elif k == 2:
            a, b = nodes[x-1]
            c, d = nodes[y-1]
            stack = deque()
            stack.append((a,b))
            seen = set()
            while len(stack) > 0 and (c, d) not in seen:
                cur, dest = stack.pop()
                seen.add((cur, dest))
                for m, n in graph[(cur, dest)]:
                    if (m, n) not in seen:
                        stack.append((m, n))
            if (c, d) in seen:
                print('YES')
            else:
                print('NO')


def __starting_point():
    solve()

__starting_point()
