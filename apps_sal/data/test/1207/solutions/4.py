from sys import stdin, stdout
import sys
import bisect
import heapq
input = sys.stdin.readline


def solve(n, m, edges):

    lo = 0
    hi = m

    curr_k = -1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        can_do = True

        adj_list = {x: [] for x in range(0, n)}
        in_degree = [0] * n
        for ed in range(min(mid, len(edges))):
            edge = edges[ed]
            adj_list[edge[0]].append(edge[1])
            in_degree[edge[1]] += 1
        candidates = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                candidates.append(i)
        res = []
        while candidates:
            ele = candidates.pop(0)
            if len(candidates) > 0:
                can_do = False
                break
            res.append(ele)
            for i in adj_list[ele]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    candidates.append(i)

        if len(res) < n:
            can_do = False

        if can_do:
            curr_k = mid
            hi = mid - 1
        else:
            lo = mid + 1

    return curr_k


def main():
    n, m = list(map(int, input().split()))

    edges = []
    for i in range(m):
        a, b = list(map(int, input().split()))
        edges.append([a - 1, b - 1])
    stdout.write(str(solve(n, m, edges)))
    stdout.write("\n")


def __starting_point():
    main()


__starting_point()
