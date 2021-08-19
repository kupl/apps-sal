def abc054c_one_stroke_path():
    import itertools
    (n, m) = map(int, input().split())
    e = [set() for _ in range(n + 1)]
    for _ in range(m):
        (a, b) = map(int, input().split())
        e[a].add(b)
        e[b].add(a)
    pattern = itertools.permutations(range(2, n + 1))
    cnt = 0
    for p in pattern:
        p_m = [1] + list(p)
        for i in range(n - 1):
            if p_m[i + 1] not in e[p_m[i]]:
                break
        else:
            cnt += 1
    print(cnt)


abc054c_one_stroke_path()
