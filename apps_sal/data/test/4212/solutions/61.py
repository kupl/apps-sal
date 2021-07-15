import itertools

def abc165c_many_requirements():
    n, m, q = map(int, input().split())
    all_list = []
    for _ in range(q):
        all_list.append(list(map(int, input().split())))

    pattern = itertools.combinations_with_replacement(range(1, m+1), n)
    best = 0
    for p in pattern:
        cost = 0
        for l in all_list:
            if p[l[1]-1] - p[l[0]-1] == l[2]:
                cost += l[3]
        if cost > best:
            best = cost
    print(best)

abc165c_many_requirements()
