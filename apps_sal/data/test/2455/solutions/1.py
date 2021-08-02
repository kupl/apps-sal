#!/usr/bin/env python3

def read_ints():
    return list(map(int, input().strip().split()))


t, = read_ints()

for _ in range(t):
    x = input()

    correct = []

    for a in [1, 2, 3, 4, 6, 12]:
        cor = False
        for c in range(0, 12 // a):
            s = set(x[c::12 // a])

            if len(s) == 1 and 'X' in s:
                cor = True
                break

        if cor == True:
            correct.append("{}x{}".format(a, 12 // a))

    print(len(correct), ' '.join(correct))
