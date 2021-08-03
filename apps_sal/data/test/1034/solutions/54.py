from heapq import heappop, heappush


def main():
    def push(i, j, k):
        nonlocal A, B, C, ADD
        if i >= x or j >= y or k >= z:
            return
        if (i, j, k) not in ADD:
            heappush(H, (A[i] + B[j] + C[k], i, j, k))
            ADD.add((i, j, k))
    x, y, z, k = list(map(int, input().split()))
    INF = 10 ** 11
    A = sorted(list([-int(x) for x in input().split()]))
    B = sorted(list([-int(x) for x in input().split()]))
    C = sorted(list([-int(x) for x in input().split()]))
    H = []
    ADD = set()
    push(0, 0, 0)
    for _ in range(k):
        ans, i, j, k = heappop(H)
        push(i + 1, j, k)
        push(i, j + 1, k)
        push(i, j, k + 1)
        print((-ans))


def __starting_point():
    main()


__starting_point()
