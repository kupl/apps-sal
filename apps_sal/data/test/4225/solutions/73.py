def i_input():
    return int(input())


def i_map():
    return list(map(int, input().split()))


def i_list():
    return list(map(int, input().split()))


def i_row(N):
    return [int(input()) for _ in range(N)]


def i_row_list(N):
    return [list(map(int, input().split())) for _ in range(N)]


(a, b, c, k) = i_map()
if k <= a:
    print(k)
elif k <= a + b:
    print(a)
else:
    print(a - (k - a - b))
