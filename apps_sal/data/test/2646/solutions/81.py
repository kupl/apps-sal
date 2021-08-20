def abc168d_double_dots():
    (n, m) = map(int, input().split())
    path_dict = {}
    for _ in range(m):
        (a, b) = map(int, input().split())
        if b not in path_dict.keys():
            path_dict[b] = [a]
        else:
            path_dict[b].append(a)
        (a, b) = (b, a)
        if b not in path_dict.keys():
            path_dict[b] = [a]
        else:
            path_dict[b].append(a)
    q = [1]
    cnt = 0
    ans = [0] * n
    ans[0] = 1
    while len(q) != 0:
        no = q.pop(0)
        for next_room in path_dict[no]:
            if ans[next_room - 1] == 0:
                ans[next_room - 1] = no
                q.append(next_room)
                cnt += 1
    if cnt != n - 1:
        print('No')
        return
    print('Yes')
    for a in ans[1:]:
        print(a)


abc168d_double_dots()
