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


(tHP, tATK, aHP, aATK) = i_map()
while True:
    aHP = max(aHP - tATK, 0)
    if aHP == 0:
        ans = 'Yes'
        break
    tHP = max(tHP - aATK, 0)
    if tHP == 0:
        ans = 'No'
        break
print(ans)
