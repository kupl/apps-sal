from heapq import heappush, heappop
from copy import deepcopy


def main():
    n = int(input())
    s = list(map(int, input().split()))

    left = []
    for e in s:
        heappush(left, -e)
    mx = heappop(left)

    made = []
    heappush(made, mx)

    for _ in range(n):
        made_prev = deepcopy(made)
        tmp = []

        while made_prev:
            made_val = heappop(made_prev)
            while left and left[0] <= made_val:
                pp = heappop(left)
                tmp.append(pp)

            if not left:
                print("No")
                return

            left_val = heappop(left)
            heappush(made, left_val)

        for e in tmp:
            heappush(left, e)

    print("Yes")


def __starting_point():
    main()

__starting_point()
