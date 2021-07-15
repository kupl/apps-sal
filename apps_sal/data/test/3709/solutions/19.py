def test(masks, wanted):
    for w in wanted:
        if w not in masks:
            return False
    return True

def any_test(masks, tests):
    for t in tests:
        if test(masks, t):
            return True
    return False

def inflate(perm):
    count = max(perm)
    masks = [[0 for i in range(len(perm))] for j in range(count)]

    for i in range(len(perm)):
        if perm[i] == 0:
            continue
        masks[perm[i] - 1][i] = 1
    return [tuple(m) for m in masks]

def gen(st, lev, teams, tests):
    if lev >= teams:
        if max(st) > 1:
            tests.append(inflate(st))
        return

    for i in range(teams + 1):
        st[lev] = i
        gen(st, lev + 1, teams, tests)

def gen_tests(teams):
    tests = []
    st = [0 for i in range(teams)]

    gen(st, 0, teams, tests)
    return tests

def back(masks, teams):
    tests = gen_tests(teams)
    return any_test(masks, tests)

def main():
    probs, teams = list(map(int, input().split()))
    masks = set()
    
    for i in range(probs):
        conf = tuple(list(map(int, input().split())))
        if 1 not in conf:
            print('YES')
            return
        masks.add(conf)

    if teams == 1:
        print('NO')
        return

    if teams == 2:
        good = test(masks, [(0, 1), (1, 0)])
    else:
        good = back(masks, teams)

    print('YES' if good else 'NO')

main()

