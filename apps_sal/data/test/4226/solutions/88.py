def i_input():
    return int(input())


def i_map():
    return map(int, input().split())


def i_list():
    return list(map(int, input().split()))


def i_row(N):
    return [int(input()) for _ in range(N)]


def i_row_list(N):
    return [list(map(int, input().split())) for _ in range(N)]


(x, y) = i_map()
ans = 'No'
for i in range(x + 1):
    if 2 * i + 4 * (x - i) == y:
        ans = 'Yes'
        break
print(ans)
