import math


def main():
    buf = input()
    buflist = buf.split()
    n = int(buflist[0])
    m = int(buflist[1])
    sr = []
    for i in range(n):
        buf = input()
        buflist = buf.split()
        sr.append((int(buflist[0]) - 1, int(buflist[1])))  # zero indexing
    sr = list(reversed(list(sorted(sr, key=lambda x: x[1]))))
    sp_list = []
    for i in range(m):
        sp_list.append([])
    for i in sr:
        sp_list[i[0]].append(i[1])
    sp_list = list(reversed(list(sorted(sp_list, key=lambda x: len(x)))))
    while len(sp_list[-1]) == 0:
        sp_list.pop()  # remove empty subject
    score_list = []
    for i, _ in enumerate(sp_list):
        score_list.append(0)
    max_level = 0
    st_idx = 0
    while len(sp_list) > 0:
        level = 0
        for i, _ in enumerate(sp_list):
            score_list[i] += sp_list[i][st_idx]
            if score_list[i] > 0:
                level += score_list[i]
        if level > max_level:
            max_level = level
        st_idx += 1
        while len(sp_list) > 0:
            if len(sp_list[-1]) <= st_idx:
                sp_list.pop()
                score_list.pop()
            else:
                break
    print(max_level)


def __starting_point():
    main()


__starting_point()
