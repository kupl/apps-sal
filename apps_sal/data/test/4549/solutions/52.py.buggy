import sys


def check(i, j, s_list, h, w):
    uesita_list = [-1, 1]
    sayuu_list = [-1, 1]

    for uesita in uesita_list:
        new_i = i + uesita
        if new_i < 0 or new_i > h - 1:
            continue
        if s_list[new_i][j] == "#":
            return True

    for sayuu in sayuu_list:
        new_j = j + sayuu
        if new_j > w - 1 or new_j < 0:
            continue
        if s_list[i][new_j] == "#":
            return True

    return False


input = sys.stdin.readline

h, w = list(map(int, input().split()))

s_list = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    w_s_list = input()
    w_s_list = w_s_list.replace('\n', '')
    w_s_list = list(w_s_list)
    for j in range(w):
        s_list[i][j] = w_s_list[j]


for i in range(h):
    for j in range(w):
        s = s_list[i][j]
        if s == "#":
            ok_flag = check(i, j, s_list, h, w)
            if not ok_flag:
                print("No")
                return

print("Yes")
