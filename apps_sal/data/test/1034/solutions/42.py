from heapq import heappush, heappop
from collections import defaultdict


def main():
    X, Y, Z, K = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    C = list(map(int, input().split(' ')))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    que = [(- A[0] - B[0] - C[0], 0, 0, 0)]  # multiply -1 to change min to max
    already_inserted = defaultdict(int)
    answer = list()
    for _ in range(K):
        q, i, j, k = heappop(que)
        answer.append(-q)
        if i + 1 < X:
            item_a = (- A[i + 1] - B[j] - C[k], i + 1, j, k)
            if already_inserted[item_a] == 0:
                heappush(que, item_a)
                already_inserted[item_a] = 1
        if j + 1 < Y:
            item_b = (- A[i] - B[j + 1] - C[k], i, j + 1, k)
            if already_inserted[item_b] == 0:
                heappush(que, item_b)
                already_inserted[item_b] = 1
        if k + 1 < Z:
            item_c = (- A[i] - B[j] - C[k + 1], i, j, k + 1)
            if already_inserted[item_c] == 0:
                heappush(que, item_c)
                already_inserted[item_c] = 1
    for ans in answer:
        print(ans)


def __starting_point():
    main()

__starting_point()
