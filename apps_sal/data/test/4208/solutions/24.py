def main():
    n = int(input())
    l = input().strip()
    r = input().strip()
    pairs = solve(n, l, r)
    print(len(pairs))
    print('\n'.join((' '.join((str(xx) for xx in x)) for x in pairs)))


def solve(n, l, r):
    from collections import deque
    answer = deque()
    l_enum_by_color = count([x for x in enumerate(l)])
    r_enum_by_color = count([x for x in enumerate(r)])
    l_q_list = l_enum_by_color.pop('?') if '?' in l_enum_by_color else deque()
    r_q_list = r_enum_by_color.pop('?') if '?' in r_enum_by_color else deque()
    for key in l_enum_by_color:
        if key not in r_enum_by_color:
            continue
        to_take_count = min(len(l_enum_by_color[key]), len(r_enum_by_color[key]))
        for _ in range(to_take_count):
            answer.append((l_enum_by_color[key].popleft(), r_enum_by_color[key].popleft()))
    for key in l_enum_by_color:
        if len(l_enum_by_color[key]) == 0:
            continue
        to_take_count = min(len(l_enum_by_color[key]), len(r_q_list))
        for _ in range(to_take_count):
            answer.append((l_enum_by_color[key].popleft(), r_q_list.popleft()))
    for key in r_enum_by_color:
        if len(r_enum_by_color[key]) == 0:
            continue
        to_take_count = min(len(r_enum_by_color[key]), len(l_q_list))
        for _ in range(to_take_count):
            answer.append((l_q_list.popleft(), r_enum_by_color[key].popleft()))
    for _ in range(min(len(l_q_list), len(r_q_list))):
        answer.append((l_q_list.popleft(), r_q_list.popleft()))
    return answer


def count(it):
    from collections import deque
    d = {}
    for a in it:
        if a[1] in d:
            d[a[1]].append(a[0] + 1)
        else:
            d[a[1]] = deque([a[0] + 1])
    return d


main()
