from collections import Counter
import heapq as hp
import sys
input = sys.stdin.readline


def main():

    N = int(input())
    A = list(map(int, input().split()))
    graph = [[] for _ in range(1 << N)]

    for l in range(N):
        for n in range(1 << l):
            graph[n].append(n + (1 << l))

    C = Counter(A)
    Keys = sorted(C.keys(), reverse=True)

    q = [(-len(graph[0]), 0)]
    for key in Keys:
        num = C[key]
        if num > len(q):
            return False
        use = []
        for _ in range(num):
            _, p = hp.heappop(q)
            use.append(p)
        for p in use:
            for np in graph[p]:
                hp.heappush(q, (-len(graph[np]), np))

    return True


def __starting_point():
    print("Yes" if main() else "No")


__starting_point()
