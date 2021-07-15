import sys
import heapq

input = sys.stdin.readline


def main():
    X, Y, Z, K = list(map(int, input().split()))
    A = list([-int(x) for x in input().split()])
    B = list([-int(x) for x in input().split()])
    C = list([-int(x) for x in input().split()])

    A.sort()
    B.sort()
    C.sort()

    p_queue = [(A[0] + B[0] + C[0], 0, 0, 0)]
    visited = set()
    visited.add((0, 0, 0))
    ans = []
    while len(ans) < K:
        s, i_A, i_B, i_C = heapq.heappop(p_queue)
        ans.append(-s)
        if i_A < X - 1 and (i_A + 1, i_B, i_C) not in visited:
            visited.add((i_A + 1, i_B, i_C))
            t = s - A[i_A] + A[i_A + 1]
            heapq.heappush(p_queue, (t, i_A + 1, i_B, i_C))
        if i_B < Y - 1 and (i_A, i_B + 1, i_C) not in visited:
            visited.add((i_A, i_B + 1, i_C))
            t = s - B[i_B] + B[i_B + 1]
            heapq.heappush(p_queue, (t, i_A, i_B + 1, i_C))
        if i_C < Z - 1 and (i_A, i_B, i_C + 1) not in visited:
            visited.add((i_A, i_B, i_C + 1))
            t = s - C[i_C] + C[i_C + 1]
            heapq.heappush(p_queue, (t, i_A, i_B, i_C + 1))

    print(("\n".join(map(str, ans))))


def __starting_point():
    main()

__starting_point()
