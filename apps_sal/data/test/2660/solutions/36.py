from heapq import heappush, heappop


def main():
    Q = int(input())

    ab_list = []
    query_type = []

    for i in range(Q):
        query = list(map(int, input().split()))
        query_type.append(query[0])
        if query[0] == 1:
            ab_list.append((query[1], query[2]))

    # query_type->[1,1,2,1,2]
    # ab_list->[(a,b),(a,b),(a,b)]

    L = []
    R = []

    ini = 0

    counter = 0
    ab_pointer = 0
    minF = 0
    for i in query_type:
        if i == 1:
            a_new = ab_list[ab_pointer][0]
            b_new = ab_list[ab_pointer][1]
            heappush(L, -1 * a_new)
            heappush(R, a_new)
            Lmax = -1 * heappop(L)
            Rmin = heappop(R)
            if Lmax <= Rmin:
                heappush(L, -1 * Lmax)
                heappush(R, Rmin)
            else:
                heappush(L, -1 * Rmin)
                heappush(R, Lmax)
            delta = abs(Lmax - Rmin)
            minF += delta + b_new
            ab_pointer += 1
        else:
            minX = -1 * heappop(L)
            print((str(minX) + " " + str(minF)))
            heappush(L, -1 * minX)


def __starting_point():
    main()


__starting_point()
