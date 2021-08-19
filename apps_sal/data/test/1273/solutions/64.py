def main():
    N = int(input())
    vertex = [[] for i in range(N)]
    ini_v = 0
    for i in range(N - 1):
        (a, b) = [int(x) for x in input().split(' ')]
        if i == 0:
            ini_v = a - 1
        vertex[a - 1].append({'v': b - 1, 'e': i})
        vertex[b - 1].append({'v': a - 1, 'e': i})
    checked_v = [0] * N
    checked_e = [0] * (N - 1)
    to_visit = [ini_v]
    checked_v[ini_v] = 1
    color_e = [-1] * (N - 1)
    while len(to_visit):
        visiting = to_visit.pop(0)
        vs = vertex[visiting]
        used_cs = []
        cless_e = []
        for d in vs:
            if checked_v[d['v']] == 0:
                checked_v[d['v']] = 1
                to_visit.append(d['v'])
            if color_e[d['e']] == -1:
                cless_e.append(d['e'])
            else:
                used_cs.append(color_e[d['e']])
        s = 0
        for j in range(len(vs)):
            if s >= len(cless_e) or len(cless_e) == 0:
                break
            elif j in used_cs:
                continue
            else:
                color_e[cless_e[s]] = j
                s += 1
    print(max(color_e) + 1)
    for i in range(len(color_e)):
        print(color_e[i] + 1)


main()
