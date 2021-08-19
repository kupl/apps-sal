def new_pos(pos, step):
    if step == 'N':
        pos = (pos[0], pos[1] + 1)
    elif step == 'S':
        pos = (pos[0], pos[1] - 1)
    elif step == 'W':
        pos = (pos[0] + 1, pos[1])
    else:
        pos = (pos[0] - 1, pos[1])
    return pos


t = int(input())
for _ in range(t):
    ans = 0
    s = input()
    used_hor = set()
    used_ver = set()
    pos = (0, 0)
    n = len(s)
    for i in range(n):
        next_st = new_pos(pos, s[i])
        way = (min(pos[0], next_st[0]), min(pos[1], next_st[1]))
        if s[i] == 'N' or s[i] == 'S':
            if way in used_ver:
                ans += 1
            else:
                ans += 5
            used_ver.add(way)
        else:
            if way in used_hor:
                ans += 1
            else:
                ans += 5
            used_hor.add(way)
        pos = next_st
    print(ans)
