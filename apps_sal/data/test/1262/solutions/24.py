import sys
readline = sys.stdin.readline


def rdw():
    return readline().rstrip()


def rdws():
    return readline().split()


def rdwl():
    return list(readline().split())


def rdi():
    return int(readline())


def rdis():
    return list(map(int, readline().split()))


def rdil():
    return list(map(int, readline().split()))


def rdilrows(cnt):
    return [rdil() for _ in range(cnt)]


def solve():
    res = 0
    bld = []
    wire = []
    n = rdi()
    cities = rdilrows(n)
    c = rdil()
    p = [-1 for i in range(n)]
    k = rdil()
    used = set()
    used.add(-1)
    for i in range(n):
        (cost, bst) = min([(c[i], i) for i in range(n) if i not in used])
        par = p[bst]
        used.add(bst)
        res += cost
        if par == -1:
            bld.append(bst + 1)
        else:
            wire.append((bst + 1, par + 1))
        for j in range(n):
            if j not in used:
                wcost = (k[bst] + k[j]) * (abs(cities[bst][0] - cities[j][0]) + abs(cities[bst][1] - cities[j][1]))
                if wcost < c[j]:
                    c[j] = wcost
                    p[j] = bst
    sys.stdout.write(f'{res}\n')
    sys.stdout.write(f'{len(bld)}\n')
    sys.stdout.write(f"{' '.join(map(str, bld))}\n")
    sys.stdout.write(f'{len(wire)}\n')
    for i in range(len(wire)):
        sys.stdout.write(f'{wire[i][0]} {wire[i][1]}\n')


tests = 1
for testnum in range(tests):
    solve()
