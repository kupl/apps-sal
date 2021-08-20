import itertools
(a, b, c) = [[0 for _ in range(2)] for _ in range(3)]
(a[0], a[1], b[0], b[1], c[0], c[1]) = [int(i) for i in input().split()]
if max(a) == max(b) == max(c) == min(a) + min(b) + min(c):
    print(max(a))
    for _ in range(min(a)):
        print(''.join(['A' for __ in range(max(a))]))
    for _ in range(min(b)):
        print(''.join(['B' for __ in range(max(a))]))
    for _ in range(min(c)):
        print(''.join(['C' for __ in range(max(a))]))
else:
    fl = False
    for i in itertools.permutations(a):
        for j in itertools.permutations(b):
            for k in itertools.permutations(c):
                for l in itertools.permutations([('A', i), ('B', j), ('C', k)]):
                    if l[0][1][1] == l[0][1][0] + l[1][1][0] and l[0][1][1] == l[1][1][1] + l[2][1][1] and (l[1][1][0] == l[2][1][0]):
                        if fl:
                            break
                        print(l[0][1][1])
                        for _ in range(l[0][1][0]):
                            print(''.join([l[0][0] for __ in range(l[0][1][1])]))
                        for _ in range(l[1][1][0]):
                            print(''.join([l[1][0] for __ in range(l[1][1][1])] + [l[2][0] for __ in range(l[2][1][1])]))
                        fl = True
    if not fl:
        print(-1)
