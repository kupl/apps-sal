def i_input(): return int(input())


def i_map(): return list(map(int, input().split()))


def i_list(): return list(map(int, input().split()))


def i_row(N): return [int(input()) for _ in range(N)]


def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]


n, m = i_map()
hh = i_list()
ab = i_row_list(m)
t = [1] * n
for a, b in ab:
    if hh[a - 1] <= hh[b - 1]:
        t[a - 1] = 0
    if hh[b - 1] <= hh[a - 1]:
        t[b - 1] = 0
print((sum(t)))
