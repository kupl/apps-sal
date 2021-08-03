import math


def is_left_son(num):
    if num == num // 2 * 2:
        return True
    else:
        return False


def bin_search(place, depth):
    answer = ""
    length = 2 ** depth
    while length > 1:
        if place > length / 2:
            answer += "R"
            place -= length / 2
        else:
            answer += "L"
        length = length / 2
    return answer


def traverse(depth, route):
    answer = 0
    cur_vert = 1
    cur_dir = "L"
    while route:
        if route[0] == "R":
            cur_vert = cur_vert * 2 + 1
        else:
            cur_vert = cur_vert * 2
        if cur_dir == route[0]:
            answer += 1
        else:
            answer += 2**depth
        depth -= 1
        route = route[1:]
        cur_dir = "R" if is_left_son(cur_vert) else "L"
    return answer


h, n = (int(x) for x in input().split())
amount_visited = 0
cur_pos = 1
print(traverse(h, bin_search(n, h)))
