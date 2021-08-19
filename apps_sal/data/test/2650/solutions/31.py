import sys
import bisect
import heapq
N_MAX = 2 * 10 ** 5
A_MAX = 10 ** 9
A = []
B = []
BB = [[] for _ in range(N_MAX)]
BBmax = []


def max_rate_in_a_kg(kg):
    while BB[kg]:
        (rate, k) = BB[kg][0]
        if B[k] == kg:
            return -rate
        else:
            heapq.heappop(BB[kg])
    return 0


def max_rate():
    while BBmax:
        (rate, kg_no) = BBmax[0]
        if max_rate_in_a_kg(kg_no) == rate:
            return rate
        else:
            heapq.heappop(BBmax)
    return None


def p():
    for i in range(len(BB)):
        if BB[i] != []:
            print(i, BB[i])


def pp():
    print('BBmax : ', end='')
    for i in range(len(BBmax)):
        print(BBmax[i], end=' ')
    print()


def main():
    (N, Q) = map(int, sys.stdin.readline().split())
    for i in range(N):
        (a, b) = map(int, sys.stdin.readline().split())
        A.append(a)
        B.append(b - 1)
        heapq.heappush(BB[b - 1], (-a, i))
    for kg_no in range(N_MAX):
        rate = max_rate_in_a_kg(kg_no)
        if rate > 0:
            BBmax.append((rate, kg_no))
    heapq.heapify(BBmax)
    for i in range(Q):
        (c, d) = map(int, sys.stdin.readline().split())
        kid_no = c - 1
        after = d - 1
        before = B[kid_no]
        B[kid_no] = after
        heapq.heappush(BB[after], (-A[kid_no], kid_no))
        new_rate_kg = max_rate_in_a_kg(before)
        if new_rate_kg != 0:
            heapq.heappush(BBmax, (new_rate_kg, before))
        new_rate_kg = max_rate_in_a_kg(after)
        if new_rate_kg != 0:
            heapq.heappush(BBmax, (new_rate_kg, after))
        print(max_rate())


def __starting_point():
    main()


__starting_point()
